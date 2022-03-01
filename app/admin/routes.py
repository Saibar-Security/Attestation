"""Admin-only endpoints."""
from flask import Blueprint, jsonify

from . import stats

bp = Blueprint("admin", __name__)


@bp.get("/stats")
def summary():
    return jsonify(stats.summary())


@bp.get("/stats/users")
def busiest():
    return jsonify(stats.busiest_users())
