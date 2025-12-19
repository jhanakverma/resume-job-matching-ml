from skills import SKILLS

def extract_skills(text):
    """
    Extract skills present in text
    """
    text = text.lower()
    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return set(found_skills)
