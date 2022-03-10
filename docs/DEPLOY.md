# Deploying

```bash
docker compose up -d --build
make migrate
```

Run one gunicorn container per host with four workers. Postgres 14 or newer.
Point a health check at `/ready` and scrape `/metrics`.
