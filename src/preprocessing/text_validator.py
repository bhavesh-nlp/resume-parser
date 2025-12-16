def is_valid_text(text: str, min_length: int = 100) -> bool:
    return bool(text and len(text.strip()) >= min_length)
