import os
import json
import time
import urllib.request
import urllib.error

DATA_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_json(url, timeout=15):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                if resp.status == 200:
                    return json.loads(resp.read().decode('utf-8', errors='ignore'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 3 * (attempt + 1)
                print(f"Rate limited (429), waiting {wait_time}s...")
                time.sleep(wait_time)
            elif e.code in [404, 403, 410]:
                print(f"HTTP {e.code} for {url}")
                return None
            else:
                time.sleep(2)
        except Exception as e:
            time.sleep(2)
    return None

def process_topic(tid_str, slug):
    tid = int(tid_str)
    target_file = os.path.join(DATA_RAW_DIR, f"topic_fetched_wow_{tid}.json")
    if os.path.exists(target_file):
        return tid, True, "Already exists"

    url = f"https://us.forums.blizzard.com/en/wow/t/{tid}.json"
    data = fetch_json(url)
    if not data or not isinstance(data, dict):
        return tid, False, "Empty or invalid response"

    post_stream = data.get("post_stream", {})
    stream_ids = post_stream.get("stream", [])
    posts = post_stream.get("posts", [])

    if len(stream_ids) > len(posts):
        loaded_ids = {p.get("id") for p in posts if "id" in p}
        missing_ids = [pid for pid in stream_ids if pid not in loaded_ids][:80]
        if missing_ids:
            query_str = "&".join([f"post_ids[]={pid}" for pid in missing_ids])
            posts_url = f"https://us.forums.blizzard.com/en/wow/t/{tid}/posts.json?{query_str}"
            time.sleep(1.0)
            p_data = fetch_json(posts_url)
            if p_data and "post_stream" in p_data:
                extra_posts = p_data["post_stream"].get("posts", [])
                posts.extend(extra_posts)
        data["post_stream"]["posts"] = posts

    data["jogo"] = "World of Warcraft"
    data["fonte"] = "Fórum Oficial"
    data["seccao"] = "Fórum Blizzard"
    data["url_fonte"] = f"https://us.forums.blizzard.com/en/wow/t/{slug}/{tid}"

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return tid, True, f"Saved ({len(posts)} posts)"

def main():
    missing_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "missing_blizzard.json")
    with open(missing_file) as f:
        targets = json.load(f)

    print(f"Fetching remaining {len(targets)} Blizzard topics sequentially with delay...")
    success = 0
    for tid, slug in targets.items():
        ok_tid, ok, msg = process_topic(tid, slug)
        status_str = "OK" if ok else "FAIL"
        print(f"[{status_str}] Topic {tid}: {msg}")
        if ok:
            success += 1
        time.sleep(2.0)

    print(f"Fetch completed: {success}/{len(targets)} succeeded.")

if __name__ == "__main__":
    main()
