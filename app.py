from fastapi import FastAPI
from routes.hd import router as hd_router

app = FastAPI(
    title="Zech AI Server",
    version="1.0.0"
)

app.include_router(hd_router, prefix="/hd")

@app.get("/")
def home():
    return {
        "name": "Zech AI Server",
        "version": "1.0.0",
        "status": "online",
        "author": "ZechZero"
    }
