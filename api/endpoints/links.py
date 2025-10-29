from fastapi import APIRouter

router = APIRouter(
    prefix="/links",
    tags=["Links"]
)


@router.get("/")
async def get_links():
    return {"links": "router"}