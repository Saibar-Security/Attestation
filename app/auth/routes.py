"""Authentication endpoints."""
from flask import Blueprint, jsonify, request

from ..errors import error
from ..extensions import db
from . import tokens

bp = Blueprint("auth", __name__)


@bp.post("/register")
def register():
    body = request.get_json(silent=True) or {}
    email = body.get("email")
    if not email:
        return error("email required", 400)
    token = tokens.new_token()
    db.execute(
        "INSERT INTO users (email, token_sig) VALUES (%s, %s)",
        (email, tokens.sign(token)),
    )
    return jsonify({"token": token}), 201


@bp.post("/whoami")
def whoami():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        return error("missing token", 401)
    for row in db.query("SELECT id, email, token_sig FROM users"):
        if tokens.verify(token, row["token_sig"]):
            return jsonify({"id": row["id"], "email": row["email"]})
    return error("invalid token", 401)
