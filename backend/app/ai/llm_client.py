import os
from google import genai
from google.genai import types
from app.schemas.response import AnalysisResponse

class LLMAnalyzer:
    def __init__(self):
        # Initialize Gemini client
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("WARNING: GEMINI_API_KEY environment variable is not set.")
        self.client = genai.Client(api_key=api_key)

    def analyze(self, prompt: str) -> dict:
        try:
            response = self.client.models.generate_content(
                model='gemini-3.6-flash',
                contents=[
                    "You are an expert AI code analyzer.",
                    prompt
                ],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=AnalysisResponse,
                    temperature=0.2,
                ),
            )
            import json
            return json.loads(response.text)
        except Exception as e:
            print(f"LLM Error: {e}")
            # Fallback mock response in case of error
            return {
                "correctness_assessment": "Error during analysis.",
                "detected_issues": [str(e)],
                "time_complexity": "Unknown",
                "space_complexity": "Unknown",
                "readability_feedback": "Unknown",
                "optimization_recommendations": [],
                "modularity_recommendations": [],
                "alternative_algorithms": [],
                "overall_score": 0
            }
