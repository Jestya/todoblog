from dataclasses import dataclass
from models.default import DefaultModel


@dataclass(kw_only=True)
class Post(DefaultModel):
    user_id: int
    category_id: int | None = None
    title: str
    content: str
