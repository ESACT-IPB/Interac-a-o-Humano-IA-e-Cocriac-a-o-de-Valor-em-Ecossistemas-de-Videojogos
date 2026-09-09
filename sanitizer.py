import re

PROFANITY_PATTERNS = [
    (r"\b(f+u+c+k+(?:ing|er|ed|s)?)\b", "[censored]"),
    (r"\b(sh+i+t+(?:ty|ting|s)?)\b", "[expletive]"),
    (r"\b(b+i+t+c+h+(?:ing|es)?)\b", "[expletive]"),
    (r"\b(a+s+s+(?:hole|holes)?)\b", "[expletive]"),
    (r"\b(b+a+s+t+a+r+d+s?)\b", "[expletive]"),
    (r"\b(d+a+m+n+)\b", "[expletive]"),
    (r"\b(c+r+a+p+)\b", "[expletive]"),
    (r"\b(d+i+c+k+s?)\b", "[expletive]"),
    (r"\b(p+u+s+s+y+)\b", "[expletive]"),
    (r"\b(c+u+n+t+s?)\b", "[expletive]"),
    (r"\b(w+t+f+)\b", "[what-the]"),
    (r"\b(s+t+f+u+)\b", "[be-quiet]"),
    (r"\bsuicide\s+gank(ing|er|s)?\b", r"highsec-gank\1"),
    (r"\bsuicide\s+attack(s)?\b", r"sacrifice-attack\1"),
    (r"\bkill\s+yourself\b", "[disparaging comment]"),
    (r"\bk+y+s+\b", "[disparaging acronym]"),
    (r"\b(r+e+t+a+r+d+(?:ed|s)?)\b", "[slur]"),
    (r"\b(i+d+i+o+t+(?:ic|s)?)\b", "[insult]"),
    (r"\b(m+o+r+o+n+(?:ic|s)?)\b", "[insult]"),
]

def sanitize_text(text: str) -> str:
    if not text or not isinstance(text, str):
        return ""
    sanitized = text
    for pattern, replacement in PROFANITY_PATTERNS:
        sanitized = re.sub(pattern, replacement, sanitized, flags=re.IGNORECASE)
    return sanitized
