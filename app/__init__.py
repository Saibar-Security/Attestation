"""Application factory for Larkspur."""
from flask import Flask

from .config import Config
from .extensions import db


def create_app(config: Config | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config or Config())

    db.init_app(app)

    from .admin.routes import bp as admin_bp
    from .auth.routes import bp as auth_bp
    from .bookmarks.routes import bp as bookmarks_bp
    from .feeds.routes import bp as feeds_bp
    from .health.routes import bp as health_bp
    from .imports.routes import bp as imports_bp
    from .metrics.routes import bp as metrics_bp
    from .search.routes import bp as search_bp
    from .tags.routes import bp as tags_bp
    from .webhooks.routes import bp as webhooks_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(bookmarks_bp, url_prefix="/bookmarks")
    app.register_blueprint(tags_bp, url_prefix="/tags")
    app.register_blueprint(search_bp, url_prefix="/search")
    app.register_blueprint(feeds_bp, url_prefix="/feeds")
    app.register_blueprint(imports_bp, url_prefix="/imports")
    app.register_blueprint(webhooks_bp, url_prefix="/webhooks")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(metrics_bp, url_prefix="/metrics")

    return app
