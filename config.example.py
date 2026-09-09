import os

# API Keys
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "your-deepseek-api-key-here")
DEEPSEEK_BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com")

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Framework Metadata & Reproducibility (DART-NET)
PIPELINE_NAME = "DART-NET"
FRAMEWORK_VERSION = "2.0.0"
PROMPT_VERSION = "2026.1"
CLASSIFICATION_VERSION = "v2-dart-net"

# Confidence Thresholds
CONFIDENCE_VERY_HIGH = 0.90
CONFIDENCE_HIGH = 0.80  # Below 0.80, human_review_required is set to True
CONFIDENCE_MODERATE = 0.60  # Below 0.60, ambiguity is preferred
CONFIDENCE_LOW = 0.40

# Directory Configurations
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
DATA_INTERIM_DIR = os.path.join(BASE_DIR, "data", "interim")
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
DATA_ANALYSIS_DIR = os.path.join(BASE_DIR, "data", "analysis")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# Ensure all directories exist
for folder in [DATA_RAW_DIR, DATA_INTERIM_DIR, DATA_PROCESSED_DIR, DATA_ANALYSIS_DIR, OUTPUT_DIR, LOGS_DIR]:
    os.makedirs(folder, exist_ok=True)

# DeepSeek Models
MODEL_FLASH = "deepseek-v4-flash"
MODEL_PRO = "deepseek-v4-pro"

# Concurrency & Delay Settings
MAX_WORKERS = 30
IO_DELAY_SECONDS = 0.01
MIN_BODY_LENGTH = 50

# Temporal Boundary (Strict Study Scope: Jan 2024 - 2026)
POST_MIN_DATE = "2024-01-01T00:00:00Z"

# Discovery Keywords (Stage 1 & Theme Validation)
DISCOVERY_KEYWORDS = [
    "AI agent", "AI bot", "artificial intelligence", "autonomous agent",
    "intelligent agent", "AI-assisted", "LLM", "large language model",
    "ChatGPT", "generative AI", "autonomous bot", "AI automation",
    "intelligent bot", "AI gameplay", "AI companion", "AI assistant",
    "AI NPC", "AI character", "botting", "automation", "Claude",
    "Copilot", "MCP", "Model Context Protocol", "DeepSeek", "Ollama",
    "Qwen", "Gemini", "Windsurf", "Codex", "vibe coding", "machine learning"
]

