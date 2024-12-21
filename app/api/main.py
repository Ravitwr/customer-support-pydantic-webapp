from fastapi import APIRouter

from app.api.routes import triage
api_router = APIRouter()

api_router.include_router(triage.router, tags=["triage"])
