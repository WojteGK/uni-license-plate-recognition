from fastapi import APIRouter

router = APIRouter(
    prefix="/ratings"
)

@router.get("/")
async def get_ratings():
    return {"ratings": "router"}