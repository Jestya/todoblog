from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase


class TimestampModelMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc).isoformat(timespec="seconds")
    )
    updated_at: Mapped[datetime | None] = mapped_column(default=None, nullable=True)


class Base(DeclarativeBase):
    pass
