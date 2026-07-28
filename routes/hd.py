from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def info():
    return {
        "feature": "HD Image",
        "status": "ready"
    }
