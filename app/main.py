from fastapi import FastAPI
from app.routes.user_routes import router as UserRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the FastAPI with MongoDB"}

app.include_router(UserRouter, prefix="/user", tags=["User"])
