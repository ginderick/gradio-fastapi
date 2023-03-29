from fastapi import APIRouter

from src.text import text_endpoints
from src.translate import translate_endpoints

api_router = APIRouter()

api_router.include_router(text_endpoints.router)
api_router.include_router(translate_endpoints.router)
