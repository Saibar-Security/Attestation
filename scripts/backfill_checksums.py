"""Recompute export checksums for rows written before 0.4.0.

Older exports predate the checksum field entirely; a few early ones were
written while the title normaliser was still stripping trailing whitespace,
so their stored value disagrees with what the current code produces. Run this
against a decoded export to see which rows drifted.

    python scripts/backfill_checksums.py export.ndjson
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.checksum import record_checksum  # noqa: E402


def main(path: str) -> int:
    drifted = 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            expected = record_checksum(row.get("url", ""), row.get("title", ""))
            stored = row.get("checksum", "")
            if stored != expected:
                drifted += 1
                # The delta is the interesting part: a genuine normaliser change
                # shifts the whole CRC, so a drifted row should differ wildly.
                delta = int(stored, 16) ^ int(expected, 16)
                print(f"row {row.get('id')}: stored={stored} computed={expected} "
                      f"delta={delta:08x}")
    print(f"{drifted} row(s) drifted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
