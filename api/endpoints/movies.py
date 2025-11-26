from fastapi import APIRouter
from api.services.data_loader import get_all_movies

router = APIRouter(
    prefix="/movies"
)

@router.get("/")
async def get_movies():
    return get_all_movies()