from fastapi import APIRouter, Depends
from core.database.session import get_db
from shemas import UserSer
from sqlalchemy.ext.asyncio import AsyncSession
import models

user_router = APIRouter()


@user_router.get("/users/")
async def get_users(session: AsyncSession = Depends(get_db)):
    pass


@user_router.post("/users/", response_model=UserSer)
async def add_user(user: UserSer, session: AsyncSession = Depends(get_db)):
    db_user = models.User(
        login=user.login,
        email=user.email,
        name=user.name,
        surname=user.surname,
        password=user.password,
    )
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return UserSer(
        login=db_user.login,
        email=db_user.email,
        name=db_user.name,
        surname=db_user.surname,
        password=db_user.password,
    )
