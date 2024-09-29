# from dataclasses import dataclass, asdict
# from models.default import DefaultModel
# from models.user import User
# from models.post import Post
# import json


# # all_posts = []

# user2 = User(
#     id=2,
#     login="login2",
#     name="Dimalox",
#     email="SOME EMAffffIL",
#     surname="SOME SURNAMdsfadsE",
#     password="SOME PASSWsdafdsaORD",
# )

# post1 = Post(
#     id=2,
#     title="какая то fadgfdsgfdsgfsfg залупапня",
#     user_id=user2.id,
#     content="SOME COfdsgsdfgfdsfdsafsdNTENT",
# )


# with open("database/posts.json", "r", encoding="utf-8") as posts:
#     all_posts = json.load(posts)

# all_posts.append(asdict(post1))

# with open("database/posts.json", "w", encoding="utf-8") as posts:
#     json.dump(all_posts, posts)


names_tg = ["miwa", "dima", "akim"]
names_vk = ["oraora", "begemoth", "tarantion"]

all_names = [names_tg, names_vk]

name = "dima"


filter_func = lambda names: name if name in names else None

print(filter_func(names_tg))
# def read_names(all_names, filter_func=lambda _: True):
#     # load from json
#     result = []
#     for names in all_names:
#         if filter_func(names):
#             result.append(names)
#     return result


# file = read_names(all_names, filter_func)
# print(file)
