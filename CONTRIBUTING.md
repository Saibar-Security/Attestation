# Contributing

Run `make lint test` before opening a PR. Keep migrations forward-only and
numbered. New sync providers go in `app/integrations/` and must ship a test
using `responses`; do not hit live APIs in CI.
