"""Tag endpoints."""
from flask import Blueprint, jsonify, request

from ..errors import error
from . import service

bp = Blueprint("tags", __name__)


@bp.get("")
def index():
    return jsonify(service.all_tags())


@bp.post("")
def create():
    body = request.get_json(silent=True) or {}
    name = (body.get("name") or "").strip()
    if not name:
        return error("name required", 400)
    return jsonify(service.create(name)), 201
