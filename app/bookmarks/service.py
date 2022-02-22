"""Bookmark persistence and retrieval."""
from ..extensions import db


def create(user_id: int, url: str, title: str, note: str) -> dict:
    rows = db.query(
        "INSERT INTO bookmarks (user_id, url, title, note) "
        "VALUES (%s, %s, %s, %s) RETURNING *",
        (user_id, url, title, note),
    )
    return rows[0]


def get(user_id: int, bookmark_id: int) -> dict | None:
    rows = db.query(
        "SELECT * FROM bookmarks WHERE user_id = %s AND id = %s",
        (user_id, bookmark_id),
    )
    return rows[0] if rows else None


def list_for(user_id: int, offset: int, limit: int) -> list[dict]:
    return db.query(
        "SELECT * FROM bookmarks WHERE user_id = %s "
        "ORDER BY created_at DESC OFFSET %s LIMIT %s",
        (user_id, offset, limit),
    )


def delete(user_id: int, bookmark_id: int) -> None:
    db.execute(
        "DELETE FROM bookmarks WHERE user_id = %s AND id = %s", (user_id, bookmark_id)
    )
