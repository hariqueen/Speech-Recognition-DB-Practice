import re

__all__ = ["create_lang_text", "create_prompts_text"]

def create_lang_text(text):
    parts = re.split(r'\(([^)]+)\)/\(([^)]+)\)', text)
    if len(parts) > 1:
        text = parts[0] + parts[1] + parts[3]
    text = re.sub(r'[^\w\s.]', '', text)
    return text

def create_prompts_text(text):
    parts = re.split(r'\(([^)]+)\)/\(([^)]+)\)', text)
    if len(parts) > 1:
        text = parts[0] + parts[2] + parts[3]
    text = re.sub(r'[^\w\s]', '', text)
    return text
