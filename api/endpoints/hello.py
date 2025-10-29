from fastapi import APIRouter

router = APIRouter(
    prefix="/hello"
)


@router.get("/")
async def get_links():
    return {"Hello": "world"}