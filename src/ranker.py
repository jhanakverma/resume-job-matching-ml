from preprocess import clean_text
from embedder import get_embedding
from matcher import match_score

def rank_resumes(resumes, job_text):
    """
    Rank resumes based on similarity to job
    """

    cleaned_job = clean_text(job_text)
    job_embedding = get_embedding(cleaned_job)

    results = []

    for name, resume_text in resumes.items():
        cleaned_resume = clean_text(resume_text)
        resume_embedding = get_embedding(cleaned_resume)

        score = match_score(resume_embedding, job_embedding)

        results.append((name, score))

    # Sort by highest score first
    results.sort(key=lambda x: x[1], reverse=True)

    return results
