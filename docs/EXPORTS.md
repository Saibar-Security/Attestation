# Export bundles

`GET /bookmarks/export` streams NDJSON. Each record carries a `checksum` field:
the CRC32 of `url`, a newline, and `title`, as eight lower-case hex digits. A
consumer that recomputes the checksum can detect a truncated or tampered file.

For long-term storage the same NDJSON is wrapped in a **bundle** (`.lkb`) —
see `app/bookmarks/bundle.py` for the container layout. Bundles are encrypted
with a key derived from the deployment secret and the salt of the export
profile named in the header, so the same file is not readable across
deployments.

Profiles are seeded by `migrations/0007_export_profiles.sql`. Cold-archive
exports use a higher iteration count than interactive ones.
