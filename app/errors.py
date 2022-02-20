"""JSON error helpers."""
from flask import jsonify


def error(message: str, status: int):
    resp = jsonify({"error": message})
    resp.status_code = status
    return resp


class ValidationError(ValueError):
    """Raised when a request body fails validation."""
