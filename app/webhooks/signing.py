"""HMAC signatures for outbound webhook deliveries."""
import hashlib
import hmac
import time

from ..config import Config


def signature(body: bytes, timestamp: int | None = None) -> str:
    ts = timestamp or int(time.time())
    mac = hmac.new(
        Config().SECRET_KEY.encode(), f"{ts}.".encode() + body, hashlib.sha256
    )
    return f"t={ts},v1={mac.hexdigest()}"


def verify(body: bytes, header: str, tolerance: int = 300) -> bool:
    parts = dict(p.split("=", 1) for p in header.split(",") if "=" in p)
    try:
        ts = int(parts["t"])
    except (KeyError, ValueError):
        return False
    if abs(time.time() - ts) > tolerance:
        return False
    expected = signature(body, ts).split("v1=")[1]
    return hmac.compare_digest(expected, parts.get("v1", ""))
