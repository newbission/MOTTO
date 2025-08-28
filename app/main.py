from fastapi import FastAPI
from app.api.v1.routes.user import router as user_router

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def ping():
    return "pong"