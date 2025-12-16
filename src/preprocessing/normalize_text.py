def normalize_text(text: str) -> str:
    """
    Normalize common abbreviations and variants
    """
    replacements = {
        "ml": "machine learning",
        "dl": "deep learning",
        "ai": "artificial intelligence",
        "ci cd": "ci/cd",
        "cicd": "ci/cd",
        "nlp" : "natural language processing"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text
