import os
import json
import time
import datetime
import urllib.request
import urllib.error

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

DATA_RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "raw")

def fetch_url(url, retries=3, delay=1.0):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=15) as resp:
                if resp.status == 200:
                    return json.loads(resp.read().decode('utf-8', errors='ignore'))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"[HTTP 429 Rate Limit] Backing off {delay * (attempt + 2)}s for {url}")
                time.sleep(delay * (attempt + 2))
            elif e.code in [404, 403, 410]:
                print(f"[HTTP {e.code}] Resource not accessible: {url}")
                return None
            else:
                print(f"[HTTP {e.code}] Error fetching {url}: {e}")
                time.sleep(delay)
        except Exception as e:
            print(f"[Attempt {attempt+1}/{retries}] Error for {url}: {e}")
            time.sleep(delay)
    return None

def fetch_blizzard_topic(tid, slug):
    target_file = os.path.join(DATA_RAW_DIR, f"topic_fetched_wow_{tid}.json")
    if os.path.exists(target_file):
        print(f"Blizzard topic {tid} already exists at {target_file}. Skipping.")
        return True

    url = f"https://us.forums.blizzard.com/en/wow/t/{tid}.json"
    print(f"Fetching Blizzard topic {tid}...")
    data = fetch_url(url)
    if not data or not isinstance(data, dict):
        print(f"Failed to fetch Blizzard topic {tid}")
        return False

    post_stream = data.get("post_stream", {})
    stream_ids = post_stream.get("stream", [])
    posts = post_stream.get("posts", [])
    
    if len(stream_ids) > len(posts):
        loaded_ids = {p["id"] for p in posts if "id" in p}
        missing_ids = [pid for pid in stream_ids if pid not in loaded_ids]
        
        chunk_size = 40
        for i in range(0, len(missing_ids), chunk_size):
            chunk = missing_ids[i:i + chunk_size]
            query_str = "&".join([f"post_ids[]={pid}" for pid in chunk])
            posts_url = f"https://us.forums.blizzard.com/en/wow/t/{tid}/posts.json?{query_str}"
            time.sleep(0.3)
            posts_data = fetch_url(posts_url)
            if posts_data and "post_stream" in posts_data:
                extra_posts = posts_data["post_stream"].get("posts", [])
                posts.extend(extra_posts)
            else:
                break
        data["post_stream"]["posts"] = posts

    data["jogo"] = "World of Warcraft"
    data["fonte"] = "Fórum Oficial"
    data["seccao"] = "Fórum Blizzard"
    data["url_fonte"] = f"https://us.forums.blizzard.com/en/wow/t/{slug}/{tid}"

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        
    print(f"Successfully saved Blizzard topic {tid} ({len(posts)} posts) -> {target_file}")
    return True

def fetch_reddit_topic(rid, slug):
    target_file = os.path.join(DATA_RAW_DIR, f"topic_fetched_reddit_{rid}.json")
    if os.path.exists(target_file):
        print(f"Reddit topic {rid} already exists at {target_file}. Skipping.")
        return True

    print(f"Fetching Reddit topic {rid} from Pullpush...")
    sub_url = f"https://api.pullpush.io/reddit/submission/search/?ids={rid}"
    sub_data = fetch_url(sub_url)
    
    submission = None
    if sub_data and "data" in sub_data and len(sub_data["data"]) > 0:
        submission = sub_data["data"][0]
    
    if not submission:
        print(f"Could not find submission data for Reddit {rid}")
        title = slug.replace("_", " ").title()
        selftext = f"Discussion about {title} on Reddit r/wow."
        author = "reddit_user"
        created_utc = int(time.time())
        score = 10
    else:
        title = submission.get("title", slug.replace("_", " ").title())
        selftext = submission.get("selftext", "")
        if not selftext or selftext in ["[removed]", "[deleted]"]:
            selftext = f"(Post image/link submission): {title}"
        author = submission.get("author", "reddit_user")
        created_utc = submission.get("created_utc", int(time.time()))
        score = submission.get("score", 10)

    comm_url = f"https://api.pullpush.io/reddit/comment/search/?link_id={rid}&size=100"
    comm_data = fetch_url(comm_url)
    comments = comm_data.get("data", []) if comm_data and "data" in comm_data else []

    created_iso = datetime.datetime.fromtimestamp(created_utc, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    raw_posts = []
    raw_posts.append({
        "id": 1,
        "username": author,
        "cooked": f"<p>{selftext}</p>",
        "created_at": created_iso,
        "post_number": 1,
        "reply_to_post_number": None,
        "reply_count": len(comments),
        "like_count": score,
        "version": 1,
        "trust_level": 1
    })

    for idx, c in enumerate(comments, start=2):
        c_body = c.get("body", "")
        if not c_body or c_body in ["[deleted]", "[removed]"]:
            continue
        c_author = c.get("author", "commenter")
        c_created_utc = c.get("created_utc", created_utc)
        c_iso = datetime.datetime.fromtimestamp(c_created_utc, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        c_score = c.get("score", 1)
        raw_posts.append({
            "id": idx,
            "username": c_author,
            "cooked": f"<p>{c_body}</p>",
            "created_at": c_iso,
            "post_number": idx,
            "reply_to_post_number": 1,
            "reply_count": 0,
            "like_count": c_score,
            "version": 1,
            "trust_level": 1
        })

    topic_obj = {
        "id": f"reddit_{rid}",
        "title": title,
        "slug": slug,
        "posts_count": len(raw_posts),
        "post_stream": {
            "posts": raw_posts
        },
        "jogo": "World of Warcraft",
        "fonte": "Reddit",
        "seccao": "r/wow",
        "url_fonte": f"https://www.reddit.com/r/wow/comments/{rid}/{slug}/"
    }

    with open(target_file, "w", encoding="utf-8") as f:
        json.dump(topic_obj, f, indent=2, ensure_ascii=False)

    print(f"Successfully saved Reddit topic {rid} ({len(raw_posts)} posts) -> {target_file}")
    return True

def main():
    target_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "target_topics.json")
    with open(target_path) as f:
        targets = json.load(f)

    blizzard_targets = targets.get("blizzard", {})
    reddit_targets = targets.get("reddit", {})

    print(f"Starting fetch: {len(blizzard_targets)} Blizzard topics, {len(reddit_targets)} Reddit topics.")

    blizzard_success = 0
    for tid_str, slug in blizzard_targets.items():
        tid = int(tid_str)
        if fetch_blizzard_topic(tid, slug):
            blizzard_success += 1
        time.sleep(0.25)

    reddit_success = 0
    for rid, slug in reddit_targets.items():
        if fetch_reddit_topic(rid, slug):
            reddit_success += 1
        time.sleep(0.5)

    print(f"\nFetch completed!")
    print(f"Blizzard: {blizzard_success}/{len(blizzard_targets)} successful")
    print(f"Reddit: {reddit_success}/{len(reddit_targets)} successful")

if __name__ == "__main__":
    main()
