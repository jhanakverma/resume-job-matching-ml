from sklearn.metrics.pairwise import cosine_similarity

def match_score(resume_embedding, job_embedding):
    """
    Calculate similarity score between resume and job
    """

    # cosine_similarity expects 2D arrays
    score = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )

    return score[0][0]
