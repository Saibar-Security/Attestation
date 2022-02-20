"""Row <-> dict mapping helpers."""
from dataclasses import asdict, dataclass, field


@dataclass
class Bookmark:
    id: int
    user_id: int
    url: str
    title: str
    note: str
    created_at: str
    tags: list[str] = field(default_factory=list)

    def to_json(self) -> dict:
        return asdict(self)


@dataclass
class Tag:
    id: int
    name: str

    def to_json(self) -> dict:
        return asdict(self)


@dataclass
class Feed:
    id: int
    user_id: int
    url: str
    title: str
    etag: str = ""
    last_polled: str = ""

    def to_json(self) -> dict:
        return asdict(self)
