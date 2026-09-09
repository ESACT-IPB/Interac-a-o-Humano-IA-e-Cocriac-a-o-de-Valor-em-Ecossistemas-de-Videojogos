import urllib.request
import json
import re
import os
import time
import logging
import threading
import config
from sanitizer import sanitize_text

# Configure logging
logger = logging.getLogger("pipeline.api_client")

# Cost file lock
cost_lock = threading.Lock()

# Token pricing per million tokens in USD
PRICING = {
    config.MODEL_FLASH: {"input": 0.30, "output": 1.10},
    config.MODEL_PRO: {"input": 0.55, "output": 2.19},
    "gemini-2.5-flash": {"input": 0.075, "output": 0.30}
}

def update_cost_log(model_name, prompt_tokens, completion_tokens):
    """Thread-safe update of the cost tracking JSON file."""
    cost_file = os.path.join(config.DATA_INTERIM_DIR, "custos_pipeline.json")
    
    # Calculate costs
    rates = PRICING.get(model_name, {"input": 0.0, "output": 0.0})
    call_cost = (prompt_tokens / 1e6 * rates["input"]) + (completion_tokens / 1e6 * rates["output"])
    
    with cost_lock:
        data = {"total_cost_usd": 0.0, "calls": []}
        if os.path.exists(cost_file):
            try:
                with open(cost_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                pass
        
        data["total_cost_usd"] += call_cost
        data["calls"].append({
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "model": model_name,
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "cost_usd": call_cost
        })
        
        try:
            with open(cost_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            logger.error(f"Failed to write cost log: {e}")

def strip_think_tags(text):
    """Removes thinking tags from output text if present."""
    if not text:
        return ""
    # Remove <think>...</think> if present
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    # Remove stray opening or closing tags
    cleaned = re.sub(r"</?think>", "", cleaned, flags=re.DOTALL)
    return cleaned.strip()

def call_gemini(messages, temperature=0.0):
    """Fallback function to query Gemini API via direct urllib request."""
    api_key = config.GEMINI_API_KEY
    if not api_key:
        logger.error("Gemini API key not found in config/env. Cannot perform Gemini fallback.")
        raise ValueError("Missing GEMINI_API_KEY")
    
    # Map messages format to Gemini format
    # Gemini uses {"role": "user" or "model", "parts": [{"text": "..."}]}
    gemini_contents = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        gemini_contents.append({
            "role": role,
            "parts": [{"text": sanitize_text(msg["content"])}]
        })
        
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": gemini_contents,
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": 2048
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        logger.info("Calling Gemini API fallback...")
        with urllib.request.urlopen(req, timeout=30) as response:
            res_body = response.read().decode("utf-8")
            res_data = json.loads(res_body)
            
            # Extract text
            candidate = res_data["candidates"][0]
            text = candidate["content"]["parts"][0]["text"]
            
            # Simple token estimation
            prompt_tokens = sum(len(m["content"]) // 4 for m in messages)
            completion_tokens = len(text) // 4
            update_cost_log("gemini-2.5-flash", prompt_tokens, completion_tokens)
            
            return text, ""
    except Exception as e:
        logger.error(f"Gemini API fallback call failed: {e}")
        raise e

def call_deepseek_raw(model, messages, thinking_enabled=False, temperature=0.0, max_tokens=None):
    """Executes a direct request to the DeepSeek API using urllib."""
    url = f"{config.DEEPSEEK_BASE_URL}/chat/completions"
    
    # Configure max tokens defaults
    if max_tokens is None:
        max_tokens = 4000 if thinking_enabled else 2000
        
    # Sanitize message contents to prevent safety policy triggers
    sanitized_messages = []
    for msg in messages:
        sanitized_messages.append({
            "role": msg["role"],
            "content": sanitize_text(msg["content"])
        })

    payload = {
        "model": model,
        "messages": sanitized_messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "thinking": {"type": "enabled" if thinking_enabled else "disabled"}
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config.DEEPSEEK_API_KEY}"
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=240) as response:
        res_body = response.read().decode("utf-8")
        data = json.loads(res_body)
        
        choice = data["choices"][0]
        message = choice["message"]
        content = message.get("content", "")
        reasoning = message.get("reasoning_content", "")
        
        # Log cost
        usage = data.get("usage", {})
        prompt_tokens = usage.get("prompt_tokens", 0)
        completion_tokens = usage.get("completion_tokens", 0)
        update_cost_log(model, prompt_tokens, completion_tokens)
        
        # Strip potential think tags in content
        cleaned_content = strip_think_tags(content)
        
        return cleaned_content, reasoning

def call_llm(model, messages, thinking_enabled=False, temperature=0.0, max_tokens=None):
    """
    Unified entry point for LLM calls with robust retry/fallback:
    - Retries primary model on failure or 429
    - Falls back to the alternative DeepSeek model (Flash <-> Pro)
    - Falls back to Gemini if all DeepSeek models fail and config allows.
    """
    models_to_try = [model]
    
    # Determine the fallback model
    if model == config.MODEL_FLASH:
        models_to_try.append(config.MODEL_PRO)
    elif model == config.MODEL_PRO:
        models_to_try.append(config.MODEL_FLASH)
        
    last_exception = None
    for current_model in models_to_try:
        # We do up to 2 retries per model for network glitches or rate limit wait
        for attempt in range(2):
            try:
                content, reasoning = call_deepseek_raw(
                    model=current_model,
                    messages=messages,
                    thinking_enabled=thinking_enabled,
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                return content, reasoning
            except urllib.error.HTTPError as e:
                last_exception = e
                # Check status code
                if e.code == 429:
                    logger.warning(f"Rate limit (429) hit for model {current_model}. Attempt {attempt + 1}/2. Waiting 5s...")
                    time.sleep(5)
                elif e.code == 401 or e.code == 403:
                    logger.error(f"Authentication error {e.code} for DeepSeek API. Checking fallback.")
                    break # Don't retry auth errors, try fallback model or Gemini
                else:
                    logger.warning(f"HTTP error {e.code} for model {current_model}. Attempt {attempt + 1}/2.")
                    time.sleep(2)
            except Exception as e:
                last_exception = e
                logger.warning(f"Unexpected error for model {current_model}: {e}. Attempt {attempt + 1}/2.")
                time.sleep(2)
                
    # If we get here, DeepSeek API calls completely failed
    logger.error("All DeepSeek cloud API models failed or returned quota errors.")
    
    # Try Gemini fallback if key is available
    if config.GEMINI_API_KEY:
        try:
            content, reasoning = call_gemini(messages, temperature=temperature)
            return content, reasoning
        except Exception as e:
            logger.critical(f"Gemini fallback also failed: {e}")
            raise e
    else:
        raise last_exception or RuntimeError("All models failed and no Gemini API key is configured.")
