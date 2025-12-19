def skill_match_score(resume_skills, job_skills):
    """
    Calculate skill overlap score
    """
    if not job_skills:
        return 0.0

    matched = resume_skills.intersection(job_skills)
    score = len(matched) / len(job_skills)

    return score
