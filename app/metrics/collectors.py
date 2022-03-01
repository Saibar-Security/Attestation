"""Prometheus-style text exposition."""
from __future__ import annotations

import time

_START = time.time()
_COUNTERS: dict[str, float] = {}


def incr(name: str, value: float = 1.0) -> None:
    _COUNTERS[name] = _COUNTERS.get(name, 0.0) + value


def render() -> str:
    lines = [
        "# HELP larkspur_uptime_seconds Process uptime.",
        "# TYPE larkspur_uptime_seconds gauge",
        f"larkspur_uptime_seconds {time.time() - _START:.3f}",
    ]
    for name, value in sorted(_COUNTERS.items()):
        lines.append(f"# TYPE {name} counter")
        lines.append(f"{name} {value}")
    return "\n".join(lines) + "\n"
