from fastapi import APIRouter
from api.services.data_loader import get_all_ratings

router = APIRouter(
    prefix="/ratings"
)

@router.get("/")
async def get_ratings():
    return get_all_ratings()