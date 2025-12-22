ACTION_WORDS = [
    "built", "developed", "designed", "implemented",
    "deployed", "trained", "optimized", "created"
]

def skill_strength(text, skill):
    """
    Estimate how strongly a skill is demonstrated
    """
    text = text.lower()
    occurrences = text.count(skill)

    strength = occurrences

    for word in ACTION_WORDS:
        if f"{word} {skill}" in text or f"{skill} {word}" in text:
            strength += 2

    return strength
