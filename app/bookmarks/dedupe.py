"""Collapse near-duplicate saves of the same page."""
from __future__ import annotations

from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING = {"utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
            "ref", "fbclid", "gclid", "mc_cid", "mc_eid"}


def canonical(url: str) -> str:
    parts = urlsplit(url)
    query = [(k, v) for k, v in parse_qsl(parts.query) if k.lower() not in TRACKING]
    return urlunsplit(
        (parts.scheme, parts.netloc.lower(), parts.path.rstrip("/"),
         urlencode(query), "")
    )


def group(rows: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for row in rows:
        out.setdefault(canonical(row["url"]), []).append(row)
    return out
