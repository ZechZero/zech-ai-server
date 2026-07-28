from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HDRequest(BaseModel):
    image: str

@router.post("/")
async def hd(data: HDRequest):
    return {
        "status": "success",
        "message": "Image diterima",
        "length": len(data.image)
    }
