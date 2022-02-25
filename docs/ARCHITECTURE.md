# Architecture

Larkspur is a Flask app using the application-factory pattern. Blueprints split
the surface into `auth`, `bookmarks`, `tags`, `search`, `feeds`, `imports`,
`webhooks`, `admin`, `metrics` and `health`. Persistence is a thin hand-rolled
layer over psycopg2 (`app/db.py`) rather than a full ORM, to keep the container
small and the query plans predictable.

Deployment is a single gunicorn container plus Postgres. Configuration is
entirely environment-driven; see `.env.example`.
