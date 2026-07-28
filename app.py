from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "name": "Zech AI Server",
        "version": "1.0.0",
        "status": "online"
    }
