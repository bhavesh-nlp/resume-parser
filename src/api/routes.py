import os
import shutil
from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from matching.shortlist_manager import save_shortlisted_resume
from utils.constants import SUPPORTED_FILE_TYPES
from utils.config import SHORTLIST_THRESHOLD

from ingestion.text_extractor import extract_resume_text
from preprocessing.clean_text import clean_text
from preprocessing.normalize_text import normalize_text

from matching.resume_skill_matcher import extract_resume_skills
from matching.semantic_matcher import semantic_similarity
from matching.score_calculator import final_score

from api.schemas import MatchResponse


router = APIRouter()


def is_supported_file(filename: str) -> bool:
    return any(filename.lower().endswith(ext) for ext in SUPPORTED_FILE_TYPES)


@router.post("/match", response_model=MatchResponse)
async def match_resume(
    resume: UploadFile = File(...),
    jd_text: str = Form(...),
    skills: str = Form(...)
):
    # -------- File validation --------
    if not is_supported_file(resume.filename):
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type. Allowed: {SUPPORTED_FILE_TYPES}"
        )

    # -------- Save uploaded resume temporarily --------
    temp_path = f"uploads/{resume.filename}"
    os.makedirs("uploads", exist_ok=True)

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    # -------- Resume ingestion --------
    resume_raw, _ = extract_resume_text(temp_path)
    resume_text = normalize_text(clean_text(resume_raw))

    # -------- JD preprocessing --------
    jd_text = normalize_text(clean_text(jd_text))

    # -------- Skill input --------
    required_skills = [
        s.strip().lower()
        for s in skills.split(",")
        if s.strip()
    ]

    if not required_skills:
        raise HTTPException(status_code=400, detail="No skills provided")

    # -------- Matching --------
    matched_skills = extract_resume_skills(resume_text, required_skills)
    skill_score = len(matched_skills) / len(required_skills)

    semantic_score = semantic_similarity(resume_text, jd_text)

    score = final_score(skill_score, semantic_score)


    decision = "shortlisted" if score >= SHORTLIST_THRESHOLD else "rejected"

    if decision == "shortlisted":
        result_payload = {
            "required_skills": required_skills,
            "matched_skills": matched_skills,
            "skill_score": round(skill_score, 3),
            "semantic_score": semantic_score,
            "final_score": score,
            "decision": decision
        }
        print("[DEBUG] Temp resume exists:", os.path.exists(temp_path))
        print("[DEBUG] Temp resume path:", temp_path)

        save_shortlisted_resume(
            resume_path=temp_path,
            result=result_payload
        )




    # cleanup ONLY after saving (or rejection)
    if os.path.exists(temp_path):
        os.remove(temp_path)

    return MatchResponse(
        required_skills=required_skills,
        matched_skills=matched_skills,
        skill_score=round(skill_score, 3),
        semantic_score=semantic_score,
        final_score=score,
        decision=decision
    )
