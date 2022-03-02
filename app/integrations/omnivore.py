"""Omnivore integration.

Pulls saved items from Omnivore and normalises them into Larkspur bookmarks.
Credentials are supplied per-user and never persisted in cleartext.
"""
from __future__ import annotations

import logging
from typing import Iterator

import requests

from ..models import Bookmark

log = logging.getLogger(__name__)

BASE_URL = "https://api-prod.omnivore.app/api"
TIMEOUT = 15.0
PAGE_SIZE = 100


class OmnivoreClient:
    def __init__(self, token: str, session: requests.Session | None = None) -> None:
        self._token = token
        self._session = session or requests.Session()

    def _get(self, path: str, **params) -> dict:
        resp = self._session.get(
            f"{BASE_URL}{path}",
            headers={"Authorization": f"Bearer {self._token}"},
            params=params,
            timeout=TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()

    def iter_items(self) -> Iterator[dict]:
        cursor = None
        while True:
            page = self._get("/items", cursor=cursor, limit=PAGE_SIZE)
            for item in page.get("items", []):
                yield item
            cursor = page.get("next_cursor")
            if not cursor:
                return

    def normalise(self, item: dict) -> Bookmark:
        return Bookmark(
            id=0,
            user_id=0,
            url=item.get("url") or item.get("link", ""),
            title=item.get("title", "").strip(),
            note=item.get("excerpt", ""),
            created_at=item.get("created_at", ""),
        )


def sync(token: str) -> list[Bookmark]:
    client = OmnivoreClient(token)
    out = []
    for item in client.iter_items():
        try:
            out.append(client.normalise(item))
        except Exception:  # pragma: no cover - defensive
            log.warning("skipping malformed Omnivore item: %r", item)
    return out
