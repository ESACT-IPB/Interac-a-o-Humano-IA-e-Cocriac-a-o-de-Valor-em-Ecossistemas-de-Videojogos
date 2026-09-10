import os
import json
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NETNO_FILE = os.path.join(BASE_DIR, "data", "analysis", "netnography_results.jsonl")
BACKUP_FILE = os.path.join(BASE_DIR, "data", "analysis", "netnography_results_1032_unpruned.jsonl")
LOG_FILE = os.path.join(BASE_DIR, "data", "analysis", "excluded_posts_log.json")

def main():
    if not os.path.exists(BACKUP_FILE):
        shutil.copyfile(NETNO_FILE, BACKUP_FILE)
        print(f"Backup criado: {BACKUP_FILE}")

    with open(BACKUP_FILE, "r", encoding="utf-8") as f:
        posts = [json.loads(line) for line in f if line.strip()]

    print(f"Total posts carregados: {len(posts)}")

    farming_threads = ["2324507", "508618", "481937", "1772220", "2116712", "2344742", "2053425", "2323925"]
    farming_keywords = [
        "gold farm", "pixel bot", "better fishing", "casino bot", "farming mats", "herbing", 
        "mining bot", "ore compression", "rmt problem", "ban the botters", "report bot", 
        "mining sucks", "ah changes", "auction house", "sniping"
    ]

    excluded = []
    kept = []

    for p in posts:
        pid = str(p.get("post_id") or p.get("id"))
        ai_type = p.get("ai_type")
        t_id = str(p.get("thread_id") or p.get("topic_id", ""))
        text = (p.get("title", "") + " " + p.get("text", "")).lower()
        
        dart = p.get("dart") or {}
        d = dart.get("dialogue", {}).get("score", 0)
        a = dart.get("access", {}).get("score", 0)
        r = dart.get("risk", {}).get("score", 0)
        t = dart.get("transparency", {}).get("score", 0)
        is_zero_dart = (d == 0 and a == 0 and r == 0 and t == 0)
        
        reasons = []
        if ai_type == "A6":
            reasons.append("A6_RUIDO_NAO_IA")
        if is_zero_dart:
            reasons.append("ZERO_DART")
        if ai_type == "A2" and (t_id in farming_threads or any(k in text for k in farming_keywords)):
            reasons.append("A2_FARMING_MECANICO_TRADICIONAL")
            
        if reasons:
            excluded.append({
                "post_id": pid,
                "thread_id": t_id,
                "game": p.get("game") or p.get("jogo"),
                "ai_type": ai_type,
                "dart_scores": {"d": d, "a": a, "r": r, "t": t},
                "reasons": reasons,
                "title": p.get("title", ""),
                "text_snippet": p.get("text", "")[:150]
            })
        else:
            kept.append(p)

    print(f"Posts excluídos: {len(excluded)}")
    print(f"Posts mantidos: {len(kept)}")

    with open(NETNO_FILE, "w", encoding="utf-8") as f:
        for p in kept:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "total_original": len(posts),
            "total_excluded": len(excluded),
            "total_refined": len(kept),
            "excluded_posts": excluded
        }, f, indent=2, ensure_ascii=False)

    print(f"Dataset refinado gravado em {NETNO_FILE} com {len(kept)} posts.")
    print(f"Log de exclusões gravado em {LOG_FILE}.")

if __name__ == "__main__":
    main()
