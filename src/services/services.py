from dataclasses import asdict
from models.post import Post
from models.user import User
from models.category import Category
import json
from serializers import PostSer, UserSer

# asdict(post1)


def read_users() -> list[User]:
    all_users = []

    with open("database/users.json", "r", encoding="utf-8") as users:
        users = json.load(users)
        for user in users:
            all_users.append(User(**user))
    return all_users


def read_posts() -> list[Post]:
    all_posts = []

    with open("database/posts.json", "r", encoding="utf-8") as posts:
        posts = json.load(posts)
        for post in posts:
            all_posts.append(Post(**post))
    return all_posts


def create_user(user: UserSer):
    old_users = read_users()
    old_users.append(User(**user.model_dump()))
    new_users = []
    for user in old_users:
        new_users.append(asdict(user))

    print(new_users)

    with open("database/users.json", "w", encoding="utf-8") as users:
        json.dump(new_users, users)

    return new_users


def create_post(post: PostSer):
    old_posts = read_posts()
    old_posts.append(Post(**post.model_dump()))
    new_posts = []
    for post in old_posts:
        new_posts.append(asdict(post))

    print(new_posts)

    with open("database/posts.json", "w", encoding="utf-8") as posts:
        json.dump(new_posts, posts)
    
    return new_posts