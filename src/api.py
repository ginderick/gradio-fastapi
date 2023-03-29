from fastapi import APIRouter

from src.text import text_endpoints

api_router = APIRouter()

api_router.include_router(text_endpoints.router)
