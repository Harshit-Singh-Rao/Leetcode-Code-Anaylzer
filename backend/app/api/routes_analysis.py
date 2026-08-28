from fastapi import APIRouter
from app.schemas.request import AnalysisRequest
from app.schemas.response import AnalysisResponse
from app.services.analysis_service import AnalysisService

router = APIRouter()
analysis_service = AnalysisService()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_code_endpoint(request: AnalysisRequest):
    result = analysis_service.analyze_code(request)
    return result
