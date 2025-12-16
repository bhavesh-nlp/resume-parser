from ingestion.text_extractor import extract_resume_text
from preprocessing.clean_text import clean_text
from preprocessing.normalize_text import normalize_text


from matching.manual_skill_input import get_employer_skills
from matching.resume_skill_matcher import extract_resume_skills
from matching.semantic_matcher import semantic_similarity
from matching.score_calculator import final_score


def main():
    from utils.config import (
        RESUME_SAMPLE_PATH,
        JD_SAMPLE_PATH,
        SKILL_WEIGHT,
        SEMANTIC_WEIGHT
    )

    resume_path = RESUME_SAMPLE_PATH
    jd_path = JD_SAMPLE_PATH


    resume_raw_text, source = extract_resume_text(resume_path)
    resume_text = normalize_text(clean_text(resume_raw_text))


    print(f"\nResume extracted using: {source}")

    with open(jd_path, "r", encoding="utf-8") as f:
        jd_raw_text = f.read()
        jd_text = normalize_text(clean_text(jd_raw_text))


    required_skills = get_employer_skills()

    if not required_skills:
        print("No skills provided. Exiting.")
        return

    matched_skills = extract_resume_skills(resume_text, required_skills)
    skill_score = len(matched_skills) / len(required_skills)

    semantic_score = semantic_similarity(resume_text, jd_text)

    score = final_score(
        skill_score=skill_score,
        semantic_score=semantic_score,
        skill_weight=SKILL_WEIGHT,
        semantic_weight=SEMANTIC_WEIGHT
    )


    print("\n========== MATCH RESULT ==========")
    print("Required Skills:", required_skills)
    print("Matched Skills:", matched_skills)
    print(f"Skill Match Score: {round(skill_score, 3)}")
    print(f"Semantic Score: {semantic_score}")
    print(f"Final Score: {score}")
    print("==================================\n")


if __name__ == "__main__":
    main()
