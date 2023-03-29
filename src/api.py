from fastapi import APIRouter

from src.chat import text_endpoints

api_router = APIRouter()

api_router.include_router(text_endpoints.router)
