from fastapi import APIRouter, Depends
from core.database.session import get_db
from shemas import UserSer
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter()


@user_router.get("/users/")
async def get_users(session: AsyncSession = Depends(get_db)):
    pass


@user_router.post("/users/")
def add_user(user: UserSer): ...
