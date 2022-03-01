"""Aggregate counters for the admin dashboard."""
from ..extensions import db

QUERIES = {
    "users": "SELECT count(*) AS n FROM users",
    "bookmarks": "SELECT count(*) AS n FROM bookmarks",
    "tags": "SELECT count(*) AS n FROM tags",
    "feeds": "SELECT count(*) AS n FROM feeds",
}


def summary() -> dict[str, int]:
    return {name: db.query(sql)[0]["n"] for name, sql in QUERIES.items()}


def busiest_users(limit: int = 10) -> list[dict]:
    return db.query(
        "SELECT user_id, count(*) AS n FROM bookmarks "
        "GROUP BY user_id ORDER BY n DESC LIMIT %s",
        (limit,),
    )
