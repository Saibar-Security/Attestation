# Known issues

## #412 — checksum mismatch on the March cold-archive bundle

`tests/data/exports/bundle_2022_03_07.lkb` decodes correctly: the container is
valid, the profile resolves, and the row count is exactly what we expect. But
49 of its 240 rows carry a `checksum` that does not match what
`app/utils/checksum.py` computes for the row sitting next to it.

The drift is not random. Every affected row is off by a small amount in the
low byte only, which is not what a title-normaliser change would do — that
would shift the whole CRC. Run the drift report against a decoded copy and
look at the `delta` column:

```bash
python scripts/backfill_checksums.py decoded.ndjson
```

Nobody has had time to work out what actually produced those values. The
round-trip test is skipped until someone does.

**Status:** open. **Owner:** unassigned.

## #380 — feed poller retries on 429 without honouring Retry-After

Low priority; the poller backs off on its own schedule and upstream has not
complained.
