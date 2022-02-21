"""Lenient timestamp parsing for imported data."""
from __future__ import annotations

import datetime

FORMATS = (
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y-%m-%dT%H:%M:%S%z",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d",
)


def parse(value: str) -> datetime.datetime | None:
    for fmt in FORMATS:
        try:
            return datetime.datetime.strptime(value, fmt)
        except (ValueError, TypeError):
            continue
    return None


def to_iso(dt: datetime.datetime) -> str:
    return dt.replace(microsecond=0).isoformat() + "Z"
