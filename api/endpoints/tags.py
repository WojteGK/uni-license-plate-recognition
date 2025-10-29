from fastapi import APIRouter

router = APIRouter(
    prefix="/tags"
)

@router.get("/")
async def get_tags():
    return {"tags": "router"}