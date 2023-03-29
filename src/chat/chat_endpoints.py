from fastapi import APIRouter

from src.chat import chat_service

router = APIRouter()


@router.get("/greet")
async def greet():

    result = chat_service.greet("Gin")
    return result
