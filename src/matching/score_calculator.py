def final_score(skill_score: float, semantic_score: float,
                skill_weight: float = 0.6,
                semantic_weight: float = 0.4):
    """
    Weighted final score
    """
    return round(
        skill_weight * skill_score +
        semantic_weight * semantic_score,
        3
    )
