"""Feed subscription endpoints."""
from flask import Blueprint, g, jsonify, request

from ..errors import error
from ..extensions import db

bp = Blueprint("feeds", __name__)


@bp.get("")
def index():
    return jsonify(db.query("SELECT * FROM feeds WHERE user_id = %s", (g.get("user_id", 0),)))


@bp.post("")
def subscribe():
    body = request.get_json(silent=True) or {}
    if not body.get("url"):
        return error("url required", 400)
    db.execute(
        "INSERT INTO feeds (user_id, url, title) VALUES (%s, %s, %s)",
        (g.get("user_id", 0), body["url"], body.get("title", "")),
    )
    return jsonify({"url": body["url"]}), 201
