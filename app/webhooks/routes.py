"""Webhook subscription management."""
from flask import Blueprint, g, jsonify, request

from ..errors import error
from ..extensions import db

bp = Blueprint("webhooks", __name__)


@bp.get("")
def index():
    return jsonify(db.query("SELECT id, endpoint FROM webhooks WHERE user_id = %s",
                            (g.get("user_id", 0),)))


@bp.post("")
def subscribe():
    body = request.get_json(silent=True) or {}
    if not body.get("endpoint", "").startswith("https://"):
        return error("endpoint must be https", 400)
    db.execute(
        "INSERT INTO webhooks (user_id, endpoint) VALUES (%s, %s)",
        (g.get("user_id", 0), body["endpoint"]),
    )
    return jsonify({"endpoint": body["endpoint"]}), 201
