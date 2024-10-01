from fastapi import APIRouter
from shemas import PostSer


post_router = APIRouter()


@post_router.get("/posts/")
def get_posts(): ...


@post_router.post("/posts/")
def add_post(post: PostSer): ...
