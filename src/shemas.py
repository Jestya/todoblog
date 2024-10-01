# pydantic models
from datetime import datetime, timezone
from pydantic import BaseModel, Field


class DefaultModel(BaseModel):
    id: int = Field(ge=0)
    created_at: datetime = datetime.now(timezone.utc).isoformat(timespec="seconds")
    updated_at: datetime | None = None


class UserSer(DefaultModel):
    login: str = Field(max_length=100)
    email: str
    name: str = Field(max_length=25)
    surname: str = Field(max_length=25)
    password: str = Field(min_length=6, description="Password must be greater than 5")


class PostSer(DefaultModel):
    user_id: int
    category_id: int | None = None
    title: str = Field(max_length=50)
    content: str


class CategorySer(DefaultModel):
    title: str = Field(max_length=50)
