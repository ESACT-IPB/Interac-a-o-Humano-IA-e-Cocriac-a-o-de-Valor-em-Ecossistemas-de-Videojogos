
import os, json, re

raw_dir = "data/raw"
raw_files = os.listdir(raw_dir)

# Read canonical topics
with open("scratch/canonical_new_topics.json") as f:
    topics = json.load(f)

already_in_raw = []
not_in_raw = []

for k, info in topics.items():
    found = False
    tid = info.get("id", "")
    ttype = info.get("type", "")
    
    for rf in raw_files:
        if tid and tid in rf:
            found = True
            already_in_raw.append((k, rf))
            break
    if not found:
        not_in_raw.append((k, info))

print(f"Total topics: {len(topics)}")
print(f"Already in data/raw: {len(already_in_raw)}")
print(f"Not in data/raw: {len(not_in_raw)}")
print("\nNot in data/raw by type:")
types_not = {}
for k, info in not_in_raw:
    t = info["type"]
    if t == "reddit": t = info.get("sub", t)
    types_not[t] = types_not.get(t, 0) + 1
for t, c in types_not.items():
    print(f"  {t}: {c}")
