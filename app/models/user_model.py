from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None

class UpdateUserSchema(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]

# MongoDB Schema for response
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user.get("age"),
    }
