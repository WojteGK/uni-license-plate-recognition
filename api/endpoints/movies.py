from fastapi import APIRouter

router = APIRouter(
    prefix="/movies"
)

@router.get("/")
async def get_movies():
    return {"movies": "router"}