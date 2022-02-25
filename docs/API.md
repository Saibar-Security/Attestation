# Larkspur API

All endpoints return JSON. Authenticate with `Authorization: Bearer <token>`.

## Auth
- `POST /auth/register` `{ "email": "..." }` -> `{ "token": "lk_..." }`
- `POST /auth/whoami` -> `{ "id", "email" }`

## Bookmarks
- `GET    /bookmarks?page=1&size=25`
- `POST   /bookmarks` `{ "url", "title?", "note?" }`
- `DELETE /bookmarks/<id>`

## Tags
- `GET  /tags`
- `POST /tags` `{ "name" }`

## Ops
- `GET /health`, `GET /ready`, `GET /metrics`
