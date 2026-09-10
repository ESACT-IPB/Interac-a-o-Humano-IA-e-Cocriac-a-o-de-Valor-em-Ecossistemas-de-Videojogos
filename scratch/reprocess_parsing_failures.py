import os
import sys
import json
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import config
from agents.netnography_agent import NetnographyAgent

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("reprocess_parsing_failures")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NETNO_FILE = os.path.join(BASE_DIR, "data", "analysis", "netnography_results.jsonl")
ANON_FILE = os.path.join(BASE_DIR, "data", "processed", "anonymized_posts.json")

def load_posts():
    with open(ANON_FILE, "r", encoding="utf-8") as f:
        posts = json.load(f)
    return {str(p.get("post_id") or p.get("id")): p for p in posts}

def identify_failed_posts():
    failed_ids = []
    with open(NETNO_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            pid = str(r.get("post_id") or r.get("id"))
            notes = (str(r.get("classification_notes", "")) + " " + 
                     str(r.get("fundamentacao_risco", "")) + " " + 
                     str(r.get("_thinking_process", ""))).lower()
            if "processing error" in notes or "expecting value" in notes or "parsing error" in notes:
                failed_ids.append(pid)
    return failed_ids

def main():
    logger.info("Iniciando identificação dos posts com falhas de parsing...")
    posts_map = load_posts()
    failed_ids = identify_failed_posts()
    logger.info(f"Total de posts com erro de parsing identificados: {len(failed_ids)}")
    
    if not failed_ids:
        logger.info("Nenhum post com falha encontrado. Todos os posts estão íntegros!")
        return

    agent = NetnographyAgent()
    reprocessed_results = {}
    
    posts_to_process = []
    for pid in failed_ids:
        if pid in posts_map:
            posts_to_process.append(posts_map[pid])
        else:
            logger.warning(f"Post ID {pid} não encontrado em anonymized_posts.json!")

    logger.info(f"A reprocessar {len(posts_to_process)} posts com deepseek-v4-flash...")

    def process_with_retry(post, max_retries=3):
        pid = str(post.get("post_id") or post.get("id"))
        res = None
        for attempt in range(1, max_retries + 1):
            try:
                res = agent.analyze_single_post(post)
                notes = (str(res.get("classification_notes", "")) + " " + 
                         str(res.get("fundamentacao_risco", ""))).lower()
                if "processing error" not in notes and "expecting value" not in notes:
                    return pid, res, True
                else:
                    logger.warning(f"Tentativa {attempt} retornou erro para {pid}, a tentar novamente...")
                    time.sleep(1)
            except Exception as e:
                logger.warning(f"Exceção na tentativa {attempt} para {pid}: {e}")
                time.sleep(1)
        return pid, res, (res is not None and "processing error" not in (str(res.get("classification_notes", "")).lower()))

    num_workers = min(15, len(posts_to_process))
    success_count = 0
    fail_count = 0

    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        futures = {executor.submit(process_with_retry, p): p for p in posts_to_process}
        for f in as_completed(futures):
            pid, res, ok = f.result()
            if res is not None:
                reprocessed_results[pid] = res
            if ok:
                success_count += 1
            else:
                fail_count += 1
            if (success_count + fail_count) % 25 == 0 or (success_count + fail_count) == len(posts_to_process):
                logger.info(f"Progresso: {success_count + fail_count}/{len(posts_to_process)} concluídos ({success_count} sucessos, {fail_count} falhas)")

    logger.info(f"Reprocessamento concluído: {success_count} com sucesso, {fail_count} com falha.")

    # Agora atualizar netnography_results.jsonl preservando a ordem original dos 1.032 posts
    logger.info("A mesclar resultados em netnography_results.jsonl...")
    updated_records = []
    with open(NETNO_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            pid = str(r.get("post_id") or r.get("id"))
            if pid in reprocessed_results:
                updated_records.append(reprocessed_results[pid])
            else:
                updated_records.append(r)

    with open(NETNO_FILE, "w", encoding="utf-8") as f:
        for r in updated_records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    logger.info(f"netnography_results.jsonl atualizado com sucesso ({len(updated_records)} registos totais).")

if __name__ == "__main__":
    main()
