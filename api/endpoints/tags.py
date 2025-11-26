from fastapi import APIRouter
from api.services.data_loader import get_all_tags
router = APIRouter(
    prefix="/tags"
)

@router.get("/")
async def get_tags():
    return get_all_tags()