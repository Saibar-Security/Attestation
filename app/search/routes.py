"""Search endpoints."""
from flask import Blueprint, g, jsonify, request

from ..extensions import db
from ..utils.pagination import page_params
from .query import parse

bp = Blueprint("search", __name__)

SQL = """
SELECT *, ts_rank(search_vector, plainto_tsquery('english', %s)) AS rank
  FROM bookmarks
 WHERE user_id = %s AND search_vector @@ plainto_tsquery('english', %s)
 ORDER BY rank DESC
 OFFSET %s LIMIT %s
"""


@bp.get("")
def search():
    raw = request.args.get("q", "")
    terms, _filters = parse(raw)
    offset, limit = page_params()
    if not terms:
        return jsonify([])
    return jsonify(db.query(SQL, (terms, g.get("user_id", 0), terms, offset, limit)))
