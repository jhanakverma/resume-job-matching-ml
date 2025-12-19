from skill_extractor import extract_skills
from skill_matcher import skill_match_score
from preprocess import clean_text
from embedder import get_embedding
from matcher import match_score

def final_score(resume_text, job_text, skill_weight=0.4):
    """
    Combine semantic similarity and skill matching
    """
    # Semantic score
    resume_clean = clean_text(resume_text)
    job_clean = clean_text(job_text)

    resume_emb = get_embedding(resume_clean)
    job_emb = get_embedding(job_clean)

    semantic = match_score(resume_emb, job_emb)

    # Skill score
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    skill_score = skill_match_score(resume_skills, job_skills)

    # Weighted final score
    final = (1 - skill_weight) * semantic + skill_weight * skill_score

    return final, semantic, skill_score
