from skill_strength import skill_strength

SECTION_WEIGHTS = {
    "experience": 1.0,
    "projects": 0.7,
    "skills": 0.4,
    "other": 0.2
}

def weighted_skill_strength(sections, skill):
    """
    Calculate skill strength weighted by resume section
    """
    total = 0.0

    for section, text in sections.items():
        strength = skill_strength(text, skill)
        total += SECTION_WEIGHTS[section] * strength

    return total
