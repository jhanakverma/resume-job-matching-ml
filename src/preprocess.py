import re

def clean_text(text):
    """
    Clean text so machine can understand it better
    """

    # 1. Make everything lowercase
    text = text.lower()

    # 2. Remove special characters (keep letters only)
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # 3. Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
