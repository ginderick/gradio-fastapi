from fastapi import APIRouter

from src.text import text_service
from src.text.text_pydantic_models import Item

router = APIRouter()


@router.post("/generate")
async def generate(item: Item):

    result = text_service.generate(item.text)
    return result
