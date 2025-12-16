def extract_resume_skills(resume_text: str, required_skills: list):
    """
    Match resume text against employer-defined skills
    """
    resume_text = resume_text.lower()
    matched = []

    for skill in required_skills:
        if skill in resume_text:
            matched.append(skill)

    return matched
