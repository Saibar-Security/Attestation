"""Opaque API-token issuing and verification."""
import hashlib
import hmac
import secrets

from ..config import Config


def new_token() -> str:
    return "lk_" + secrets.token_urlsafe(24)


def _mac(token: str, secret: str) -> str:
    return hmac.new(secret.encode(), token.encode(), hashlib.sha256).hexdigest()


def sign(token: str) -> str:
    return _mac(token, Config().SECRET_KEY)


def verify(token: str, signature: str) -> bool:
    return hmac.compare_digest(sign(token), signature)
