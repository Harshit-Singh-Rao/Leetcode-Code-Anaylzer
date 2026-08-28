from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_analysis import router as analysis_router

app = FastAPI(title="AI Coder Analyzer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/")
def read_root():
    return {
        "message": "AI Coder Analyzer API is running successfully on Vercel!",
        "docs": "Visit /docs to see the API documentation."
    }
