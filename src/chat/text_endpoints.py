from fastapi import APIRouter

from src.chat import text_service
from src.chat.text_pydantic_models import Item

router = APIRouter()


@router.post("/generate")
async def generate(item: Item):

    result = text_service.generate(item.text)
    return result
