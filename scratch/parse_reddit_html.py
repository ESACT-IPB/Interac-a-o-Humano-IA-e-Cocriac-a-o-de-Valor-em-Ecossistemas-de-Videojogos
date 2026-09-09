import re
import json
import os
import sys
from html.parser import HTMLParser

class RedditExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_post_text = False
        self.in_comment_text = False
        self.post_text_pieces = []
        self.current_comment = None
        self.comments = []
        self.post_meta = {}

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == 'shreddit-post':
            self.post_meta = {
                'title': attr_dict.get('post-title', 'Sem Título'),
                'author': attr_dict.get('author', 'Anónimo'),
                'created_at': attr_dict.get('created-timestamp', ''),
                'score': int(attr_dict.get('score', 1) or 1),
                'comment_count': int(attr_dict.get('comment-count', 0) or 0),
                'id': attr_dict.get('id', '')
            }
        elif tag == 'div' and attr_dict.get('slot') == 'text-body':
            self.in_post_text = True
        elif tag == 'shreddit-comment':
            self.current_comment = {
                'id': attr_dict.get('thingid'),
                'author': attr_dict.get('author', 'Anónimo'),
                'score': int(attr_dict.get('score', 1) or 1),
                'created_at': attr_dict.get('created', ''),
                'parent_id': attr_dict.get('parentid'),
                'text_pieces': []
            }
        elif tag == 'div' and attr_dict.get('slot') == 'comment':
            self.in_comment_text = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.in_post_text:
            self.in_post_text = False
        elif tag == 'div' and self.in_comment_text:
            self.in_comment_text = False
        elif tag == 'shreddit-comment':
            if self.current_comment:
                c_text = ' '.join(self.current_comment.pop('text_pieces')).strip()
                if c_text and c_text not in ['[deleted]', '[removed]']:
                    self.current_comment['text'] = c_text
                    self.comments.append(self.current_comment)
                self.current_comment = None

    def handle_data(self, data):
        clean_d = data.strip()
        if not clean_d:
            return
        if self.in_post_text:
            self.post_text_pieces.append(clean_d)
        elif self.in_comment_text and self.current_comment:
            self.current_comment['text_pieces'].append(clean_d)

def parse_file(html_file, rid, slug, target_dir):
    with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    extractor = RedditExtractor()
    extractor.feed(html)

    title = extractor.post_meta.get('title', slug.replace('_', ' ').title())
    author = extractor.post_meta.get('author', 'Anónimo')
    created_at = extractor.post_meta.get('created_at', '')
    score = extractor.post_meta.get('score', 1)
    post_body = ' '.join(extractor.post_text_pieces).strip()
    if not post_body:
        post_body = f"(Reddit post): {title}"

    raw_posts = []
    # OP post
    raw_posts.append({
        "id": 1,
        "username": author,
        "cooked": f"<p>{post_body}</p>",
        "created_at": created_at,
        "post_number": 1,
        "reply_to_post_number": None,
        "reply_count": len(extractor.comments),
        "like_count": score,
        "version": 1,
        "trust_level": 1
    })

    for idx, c in enumerate(extractor.comments, start=2):
        raw_posts.append({
            "id": idx,
            "username": c.get('author', 'Anónimo'),
            "cooked": f"<p>{c.get('text', '')}</p>",
            "created_at": c.get('created_at', created_at),
            "post_number": idx,
            "reply_to_post_number": 1,
            "reply_count": 0,
            "like_count": c.get('score', 1),
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

    out_file = os.path.join(target_dir, f"topic_fetched_reddit_{rid}.json")
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(topic_obj, f, indent=2, ensure_ascii=False)
    print(f"Saved Reddit topic {rid} ({len(raw_posts)} posts) -> {out_file}")

if __name__ == '__main__':
    html_f = sys.argv[1]
    rid = sys.argv[2]
    slug = sys.argv[3]
    t_dir = sys.argv[4]
    parse_file(html_f, rid, slug, t_dir)
