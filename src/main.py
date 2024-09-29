from fastapi import FastAPI
from services.services import read_posts, read_users, create_user, create_post
from serializers import UserSer, PostSer

app = FastAPI(title="blog")


@app.get("/users/")
def root():
    users = read_users()
    return users


@app.get("/posts/")
def get_posts():
    posts = read_posts()
    return posts


@app.post("/users/")
def add_user(user: UserSer):
    users = create_user(user)
    return users


@app.post("/posts/")
def add_post(post: PostSer):
    posts = create_post(post)
    return posts