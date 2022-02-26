"""Thin wrapper over feedparser with sane defaults."""
from __future__ import annotations

import feedparser


def parse(content: bytes) -> list[dict]:
    parsed = feedparser.parse(content)
    out = []
    for entry in parsed.entries:
        out.append(
            {
                "url": entry.get("link", ""),
                "title": entry.get("title", "").strip(),
                "note": entry.get("summary", "")[:500],
                "published": entry.get("published", ""),
            }
        )
    return out
