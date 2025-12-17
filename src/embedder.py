from sentence_transformers import SentenceTransformer

# Load the model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """
    Convert text into numerical embedding
    """
    embedding = model.encode(text)
    return embedding
