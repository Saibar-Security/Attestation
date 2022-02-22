"""Tag persistence."""
from ..extensions import db
from ..utils.slugify import slugify


def all_tags() -> list[dict]:
    return db.query("SELECT id, name FROM tags ORDER BY name")


def create(name: str) -> dict:
    slug = slugify(name)
    db.execute("INSERT INTO tags (name) VALUES (%s) ON CONFLICT DO NOTHING", (slug,))
    return {"name": slug}


def attach(bookmark_id: int, tag_id: int) -> None:
    db.execute(
        "INSERT INTO bookmark_tags (bookmark_id, tag_id) VALUES (%s, %s) "
        "ON CONFLICT DO NOTHING",
        (bookmark_id, tag_id),
    )
