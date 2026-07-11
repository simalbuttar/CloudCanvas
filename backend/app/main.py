from fastapi import FastAPI
from app.routes import health

app = FastAPI(
    title="CloudCanvas API",
    description="AI infrastructure platform backend",
    version="0.1.0"
)

app.include_router(health.router)


@app.get("/")
def home():
    return {
        "message": "CloudCanvas API is running 🚀",
        "version": "0.1.0"
    }