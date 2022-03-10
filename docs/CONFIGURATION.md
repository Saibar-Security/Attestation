# Configuration

| Variable | Default | Meaning |
| --- | --- | --- |
| `SECRET_KEY` | `dev-only-not-secret` | Signs API tokens and webhook payloads. |
| `DATABASE_URL` | local socket | Postgres DSN. |
| `PAGE_SIZE` | `25` | Default page size. |
| `RATE_LIMIT` | `120` | Requests per minute per token. |
| `FEED_POLL_SECONDS` | `900` | Feed poll interval. |
| `WEBHOOK_TIMEOUT` | `10` | Per-delivery timeout in seconds. |

`SECRET_KEY` must be stable across replicas or issued tokens stop verifying.
Rotating it invalidates every outstanding token and makes older export bundles
unreadable.
