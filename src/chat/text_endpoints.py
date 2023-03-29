from fastapi import APIRouter

from src.chat import text_service

router = APIRouter()


@router.get("/greet")
async def generate():

    result = text_service.generate("Gin")
    return result
