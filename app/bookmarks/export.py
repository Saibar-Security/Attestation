"""Export a user's bookmarks as newline-delimited JSON."""
from __future__ import annotations

import json

from ..utils.checksum import record_checksum
from .service import list_for

FIELDS = ("id", "user_id", "url", "title", "note", "tags", "created_at")


def to_record(row: dict) -> dict:
    out = {k: row.get(k) for k in FIELDS}
    out["checksum"] = record_checksum(out["url"] or "", out["title"] or "")
    return out


def export_ndjson(user_id: int) -> str:
    rows = list_for(user_id, 0, 100_000)
    return "\n".join(json.dumps(to_record(r), separators=(",", ": ")) for r in rows)
