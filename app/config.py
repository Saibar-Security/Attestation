"""Configuration loaded from the environment."""
import os


class Config:
    def __init__(self) -> None:
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-not-secret")
        self.DATABASE_URL = os.environ.get(
            "DATABASE_URL", "postgresql://larkspur@localhost/larkspur"
        )
        self.PAGE_SIZE = int(os.environ.get("PAGE_SIZE", "25"))
        self.RATE_LIMIT = int(os.environ.get("RATE_LIMIT", "120"))
        self.FEED_POLL_SECONDS = int(os.environ.get("FEED_POLL_SECONDS", "900"))
        self.WEBHOOK_TIMEOUT = float(os.environ.get("WEBHOOK_TIMEOUT", "10"))
