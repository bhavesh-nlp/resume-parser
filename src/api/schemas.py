from pydantic import BaseModel
from typing import List


class MatchResponse(BaseModel):
    required_skills: List[str]
    matched_skills: List[str]
    skill_score: float
    semantic_score: float
    final_score: float
    decision: str
