"""Fixed-window rate limiter (per-token, in-memory)."""
from __future__ import annotations

import time
from collections import defaultdict

_HITS: dict[str, list[float]] = defaultdict(list)


def allow(key: str, limit: int, window: float = 60.0) -> bool:
    now = time.time()
    hits = [t for t in _HITS[key] if now - t < window]
    hits.append(now)
    _HITS[key] = hits
    return len(hits) <= limit
