from fastapi import APIRouter

from src.translate.translate_pydantic_models import Item
from src.translate.translate_service import translate_service

router = APIRouter()


@router.post("/translate")
async def translate(item: Item):

    return translate_service.translate(item.text)
