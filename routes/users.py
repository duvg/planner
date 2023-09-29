from fastapi import APIRouter, HTTPException, status
from database.connection import Database

from models.user import User, UserSingIn

user_router = APIRouter(
  tags=["User"]
)

user_database = Database(User)

users = {}

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
  user_exist = await User.find_one(User.email == user.email)

  if user_exist:
    raise HTTPException(
      status_code = status.HTTP_409_CONFLICT,
      detail="User with supplied username exists"
    )

  await user_database.save(user)

  return {
    "message": "User successfully registered!"
  }

@user_router.post("/signin")
async def sign_user_in(user: UserSingIn) -> dict:
  user_exist = await User.find_one(User.email == user.email)
  if not user_exist:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail="Users does not exist"
    )

  print(user_exist.password)
  if user_exist.password == user.password:
    return {
      "message": "User signed in successfully"
    }

  raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail="Wrong credentials passed"
    )