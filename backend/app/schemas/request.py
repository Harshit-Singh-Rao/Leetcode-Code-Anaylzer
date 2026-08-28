from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    problem_statement: str
    source_code: str
    language: str
