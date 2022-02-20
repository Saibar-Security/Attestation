"""Minimal Postgres access layer."""
from __future__ import annotations

import contextlib
from typing import Any, Iterable

try:  # pragma: no cover - psycopg2 optional in tests
    import psycopg2
    import psycopg2.extras
except Exception:  # pragma: no cover
    psycopg2 = None


class Database:
    def __init__(self) -> None:
        self._dsn: str | None = None

    def init_app(self, app) -> None:
        self._dsn = app.config["DATABASE_URL"]

    @contextlib.contextmanager
    def cursor(self):
        if psycopg2 is None:
            raise RuntimeError("psycopg2 not available")
        conn = psycopg2.connect(self._dsn)
        try:
            cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            yield cur
            conn.commit()
        finally:
            conn.close()

    def query(self, sql: str, params: Iterable[Any] = ()) -> list[dict]:
        with self.cursor() as cur:
            cur.execute(sql, tuple(params))
            return list(cur.fetchall())

    def execute(self, sql: str, params: Iterable[Any] = ()) -> None:
        with self.cursor() as cur:
            cur.execute(sql, tuple(params))
