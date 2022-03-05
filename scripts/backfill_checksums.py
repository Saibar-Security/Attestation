"""Recompute export checksums for rows written before 0.4.0.

Older exports predate the checksum field entirely; a few early ones were
written while the title normaliser was still stripping trailing whitespace,
so their stored value disagrees with what the current code produces. Run this
against a decoded export to see which rows drifted.

    python scripts/backfill_checksums.py export.ndjson
"""
from __future__ import annotations

import json
import sys

from app.utils.checksum import record_checksum


def main(path: str) -> int:
    drifted = 0
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            expected = record_checksum(row.get("url", ""), row.get("title", ""))
            if row.get("checksum") != expected:
                drifted += 1
                print(f"row {row.get('id')}: stored={row.get('checksum')} "
                      f"computed={expected}")
    print(f"{drifted} row(s) drifted")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1]))
