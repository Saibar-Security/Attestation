"""Maintain the tsvector column used for ranking."""
from ..extensions import db

REINDEX = """
UPDATE bookmarks
   SET search_vector = to_tsvector('english', coalesce(title,'') || ' ' || coalesce(note,''))
 WHERE id = %s
"""


def reindex_one(bookmark_id: int) -> None:
    db.execute(REINDEX, (bookmark_id,))


def reindex_all() -> int:
    rows = db.query("SELECT id FROM bookmarks")
    for row in rows:
        reindex_one(row["id"])
    return len(rows)
