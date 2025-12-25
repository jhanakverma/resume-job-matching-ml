def split_sections(text):
    """
    Split resume into sections using common headings
    """
    text = text.lower()

    sections = {
        "experience": "",
        "projects": "",
        "skills": "",
        "other": ""
    }

    current = "other"

    for line in text.split("\n"):
        line = line.strip()

        if "experience" in line:
            current = "experience"
        elif "project" in line:
            current = "projects"
        elif "skill" in line:
            current = "skills"
        elif line == "":
            continue

        sections[current] += line + " "

    return sections
