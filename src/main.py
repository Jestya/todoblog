import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, APIRouter
from routers import posts, users
from core.database.session import Base, sessionmanager
from models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    sessionmanager.init_db()
    # async with sessionmanager.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="blog", lifespan=lifespan)


app.include_router(posts.post_router)
app.include_router(users.user_router)
