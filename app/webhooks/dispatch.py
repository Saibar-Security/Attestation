"""Deliver events to subscriber endpoints with bounded retries."""
from __future__ import annotations

import json
import logging

import requests

from ..config import Config
from ..extensions import db
from .signing import signature

log = logging.getLogger(__name__)
MAX_ATTEMPTS = 5
BACKOFF = (1, 5, 30, 120, 600)


def deliver(endpoint: str, event: str, payload: dict) -> bool:
    body = json.dumps({"event": event, "data": payload}).encode()
    for attempt in range(MAX_ATTEMPTS):
        try:
            resp = requests.post(
                endpoint,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "X-Larkspur-Signature": signature(body),
                },
                timeout=Config().WEBHOOK_TIMEOUT,
            )
            if resp.status_code < 300:
                return True
        except requests.RequestException:
            log.warning("delivery to %s failed (attempt %d)", endpoint, attempt + 1)
    return False


def fanout(user_id: int, event: str, payload: dict) -> int:
    sent = 0
    for row in db.query("SELECT endpoint FROM webhooks WHERE user_id = %s", (user_id,)):
        if deliver(row["endpoint"], event, payload):
            sent += 1
    return sent
