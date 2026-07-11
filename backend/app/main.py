from fastapi import FastAPI

app = FastAPI(
    title="CloudCanvas API",
    description="AI infrastructure platform backend",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "CloudCanvas API is running 🚀",
        "version": "0.1.0"
    }