from fastapi import APIRouter

from src.translate.translate_pydantic_models import Item

router = APIRouter()


@router.post("/translate")
async def translate(item: Item):

    return "Testing"
