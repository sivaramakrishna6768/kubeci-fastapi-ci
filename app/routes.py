from fastapi import APIRouter
from app.models import User
from app.service import get_users, add_user

user_router = APIRouter()

@user_router.get("/", response_model=list[User])
def read_users():
    return get_users()

@user_router.post("/", response_model=User)
def create_user(user: User):
    return add_user(user)
