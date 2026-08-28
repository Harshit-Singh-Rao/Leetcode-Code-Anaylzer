from app.schemas.request import AnalysisRequest
from app.schemas.response import AnalysisResponse
from app.analyzers.python.ast_analyzer import PythonASTAnalyzer
from app.ai.llm_client import LLMAnalyzer
from app.ai.prompts import build_analysis_prompt

class AnalysisService:
    def __init__(self):
        self.ast_analyzer = PythonASTAnalyzer()
        self.llm_analyzer = LLMAnalyzer()

    def analyze_code(self, request: AnalysisRequest) -> AnalysisResponse:
        ast_info = {}
        if request.language.lower() == "python":
            ast_info = self.ast_analyzer.analyze(request.source_code)
            if not ast_info.get("valid_syntax"):
                return AnalysisResponse(
                    correctness_assessment="Syntax Error detected.",
                    detected_issues=[ast_info.get("error", "Unknown syntax error")],
                    time_complexity="N/A",
                    space_complexity="N/A",
                    readability_feedback="Code does not parse.",
                    optimization_recommendations=[],
                    modularity_recommendations=[],
                    alternative_algorithms=[],
                    overall_score=0
                )

        prompt = build_analysis_prompt(
            request.problem_statement,
            request.source_code,
            request.language,
            ast_info
        )

        llm_result = self.llm_analyzer.analyze(prompt)
        return AnalysisResponse(**llm_result)
