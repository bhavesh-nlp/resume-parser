def get_employer_skills():
    """
    Employer provides required skills explicitly.
    Skills must be comma-separated.
    """
    raw = input("Enter required skills (comma separated): ")

    skills = [
        skill.strip().lower()
        for skill in raw.split(",")
        if skill.strip()
    ]

    return skills
