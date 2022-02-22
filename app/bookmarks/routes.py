"""Bookmark endpoints."""
from flask import Blueprint, g, jsonify, request

from ..config import Config
from ..errors import error
from ..utils.pagination import page_params
from . import service

bp = Blueprint("bookmarks", __name__)


@bp.get("")
def index():
    offset, limit = page_params(Config().PAGE_SIZE)
    return jsonify(service.list_for(g.get("user_id", 0), offset, limit))


@bp.post("")
def create():
    body = request.get_json(silent=True) or {}
    if not body.get("url"):
        return error("url required", 400)
    bm = service.create(
        g.get("user_id", 0), body["url"], body.get("title", ""), body.get("note", "")
    )
    return jsonify(bm), 201


@bp.delete("/<int:bookmark_id>")
def destroy(bookmark_id: int):
    service.delete(g.get("user_id", 0), bookmark_id)
    return "", 204
