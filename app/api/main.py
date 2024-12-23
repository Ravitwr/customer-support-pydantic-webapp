from fastapi import APIRouter

from app.api.routes import post
api_router = APIRouter()

api_router.include_router(post.router, tags=["post"])
