from fastapi import FastAPI
from fastapi_users import fastapi_users, FastAPIUsers
from src.auth.auth import auth_backend
from src.auth.database import User
from src.auth.schemas import UserRead, UserCreate
from src.auth.maneger import get_user_manager

app = FastAPI(
    title="Reagent Flow"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
