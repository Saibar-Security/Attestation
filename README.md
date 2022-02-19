# Larkspur

A self-hosted **read-it-later** API. Save links, tag them, search them, and
pull them back later as clean JSON.

## Features

- Token-authenticated REST API
- Bookmarks with titles, notes, and tags
- Full-text search with ranking
- Feed polling and import from a dozen other services
- Outbound webhooks with HMAC signing
- Portable, encrypted export bundles

## Quickstart

```bash
cp .env.example .env
docker compose up --build
curl localhost:8000/health
```

See `docs/API.md` for the full API, `docs/ARCHITECTURE.md` for internals, and
`docs/EXPORTS.md` for the export bundle format.
