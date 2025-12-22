from job_skill_extractor import extract_job_skills
from skill_strength import skill_strength
from preprocess import clean_text
from embedder import get_embedding
from matcher import match_score

def job_aware_score(resume_text, job_text):
    """
    Score resume based on job-required skills and semantic match
    """

    # Semantic similarity
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    semantic = match_score(
        get_embedding(resume_clean),
        get_embedding(job_clean)
    )

    # Job-required skills
    job_skills = extract_job_skills(job_text)

    if not job_skills:
        return semantic

    total_strength = 0

    for skill in job_skills:
        total_strength += skill_strength(resume_text, skill)

    skill_score = total_strength / (len(job_skills) * 3)

    final_score = 0.6 * semantic + 0.4 * skill_score

    return final_score, semantic, skill_score

