from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Resume Matching API",
    description="End-to-end resume parsing and JD matching system",
    version="1.0"
)

app.include_router(router)
