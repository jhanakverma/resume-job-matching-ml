from skills import SKILLS

def extract_job_skills(job_text):
    """
    Extract only skills that appear in the job description
    """
    job_text = job_text.lower()
    job_skills = []

    for skill in SKILLS:
        if skill in job_text:
            job_skills.append(skill)

    return set(job_skills)
