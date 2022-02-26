"""Poll subscribed feeds and insert new entries."""
from __future__ import annotations

import logging

import requests

from ..bookmarks import service
from ..extensions import db
from . import parser

log = logging.getLogger(__name__)


def poll_one(feed: dict) -> int:
    headers = {}
    if feed.get("etag"):
        headers["If-None-Match"] = feed["etag"]
    resp = requests.get(feed["url"], headers=headers, timeout=20)
    if resp.status_code == 304:
        return 0
    added = 0
    for entry in parser.parse(resp.content):
        if not entry["url"]:
            continue
        service.create(feed["user_id"], entry["url"], entry["title"], entry["note"])
        added += 1
    db.execute(
        "UPDATE feeds SET etag = %s, last_polled = now() WHERE id = %s",
        (resp.headers.get("ETag", ""), feed["id"]),
    )
    return added


def poll_all() -> int:
    total = 0
    for feed in db.query("SELECT * FROM feeds"):
        try:
            total += poll_one(feed)
        except Exception:
            log.exception("feed %s failed", feed.get("id"))
    return total
