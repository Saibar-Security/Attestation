"""Offset/limit pagination helpers."""
from flask import request


def page_params(default_size: int = 25) -> tuple[int, int]:
    try:
        page = max(1, int(request.args.get("page", 1)))
    except ValueError:
        page = 1
    try:
        size = min(100, max(1, int(request.args.get("size", default_size))))
    except ValueError:
        size = default_size
    return (page - 1) * size, size
