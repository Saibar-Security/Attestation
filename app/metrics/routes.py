"""Metrics endpoint."""
from flask import Blueprint, Response

from . import collectors

bp = Blueprint("metrics", __name__)


@bp.get("")
def metrics():
    return Response(collectors.render(), mimetype="text/plain; version=0.0.4")
