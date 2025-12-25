from job_skill_extractor import extract_job_skills
from section_parser import split_sections
from section_skill_strength import weighted_skill_strength
from preprocess import clean_text
from embedder import get_embedding
from matcher import match_score

def elite_score(resume_text, job_text):
    """
    Final human-like resume scoring
    """

    # Semantic similarity
    semantic = match_score(
        get_embedding(clean_text(resume_text)),
        get_embedding(clean_text(job_text))
    )

    job_skills = extract_job_skills(job_text)
    sections = split_sections(resume_text)

    if not job_skills:
        return semantic, semantic, 0.0

    total_strength = 0.0

    for skill in job_skills:
        total_strength += weighted_skill_strength(sections, skill)

    skill_score = total_strength / (len(job_skills) * 3)

    final_score = 0.6 * semantic + 0.4 * skill_score

    return final_score, semantic, skill_score
