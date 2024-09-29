from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(kw_only=True)
class DefaultModel:
    id: int
    created_at: datetime = datetime.now(timezone.utc).isoformat(timespec="seconds")
    updated_at: datetime | None = None
