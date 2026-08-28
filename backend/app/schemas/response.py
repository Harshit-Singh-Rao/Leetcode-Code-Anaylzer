from pydantic import BaseModel
from typing import List

class AnalysisResponse(BaseModel):
    correctness_assessment: str
    detected_issues: List[str]
    time_complexity: str
    space_complexity: str
    readability_feedback: str
    optimization_recommendations: List[str]
    modularity_recommendations: List[str]
    alternative_algorithms: List[str]
    overall_score: int
