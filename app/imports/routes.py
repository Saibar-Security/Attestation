"""Bulk import endpoints."""
from flask import Blueprint, g, jsonify, request

from ..bookmarks import service
from ..errors import error
from . import netscape

bp = Blueprint("imports", __name__)


@bp.post("/netscape")
def import_netscape():
    payload = request.get_data(as_text=True)
    if not payload:
        return error("empty body", 400)
    count = 0
    for item in netscape.parse(payload):
        service.create(g.get("user_id", 0), item["url"], item["title"], "")
        count += 1
    return jsonify({"imported": count}), 201
