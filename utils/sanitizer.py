import re

def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+', ' ', text)

def normalize_whitespace(text):
    return re.sub(r'\s+', ' ', text).strip()

def sanitize_text(text):

    text = remove_non_ascii(text)
    text = normalize_whitespace(text)

    return text
