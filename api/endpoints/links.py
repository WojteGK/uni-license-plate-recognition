from fastapi import APIRouter
from api.services.data_loader import get_all_links

router = APIRouter(
    prefix="/links",
    tags=["Links"]
)


@router.get("/")
async def get_links():
    return get_all_links()