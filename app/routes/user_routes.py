from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.controllers.user_controller import (
    retrieve_users,
    add_user,
    retrieve_user,
    update_user,
    delete_user
)
from app.models.user_model import UserSchema, UpdateUserSchema

router = APIRouter()

@router.post("/", response_description="Add new user")
async def create_user(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    return new_user

@router.get("/", response_description="List all users")
async def get_users():
    users = await retrieve_users()
    return users

@router.get("/{id}", response_description="Get a single user by ID")
async def get_user(id: str):
    user = await retrieve_user(id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{id}", response_description="Update a user")
async def update_user_data(id: str, req: UpdateUserSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return "User updated successfully"
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{id}", response_description="Delete a user")
async def delete_user_data(id: str):
    deleted = await delete_user(id)
    if deleted:
        return "User deleted successfully"
    raise HTTPException(status_code=404, detail="User not found")
