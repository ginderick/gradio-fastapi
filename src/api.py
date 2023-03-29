from fastapi import APIRouter

from src.chat import chat_endpoints

api_router = APIRouter()

api_router.include_router(chat_endpoints.router)
