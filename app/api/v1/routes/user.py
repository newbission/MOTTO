from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import login as login_test

router = APIRouter(
    prefix="/users"
)

class UserLogin(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(user_data: UserLogin):
    
    user = login_test.user_login(user_data.email, user_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    print(user)
    return {
        "message": "Success!!",
        "access_token": user["access_token"],
    }