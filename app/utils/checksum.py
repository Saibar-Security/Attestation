"""Row checksums for export integrity.

Exports carry a CRC32 of the immutable part of each row so a consumer can tell
a truncated or edited file from an intact one. Only ``url`` and ``title``
participate: notes and tags are user-editable after the fact and would make
every re-export mismatch.
"""
from __future__ import annotations

import binascii


def record_checksum(url: str, title: str) -> str:
    """CRC32 of ``url``, a newline, then ``title``. Lower-case, 8 hex digits."""
    return f"{binascii.crc32(f'{url}\n{title}'.encode()) & 0xFFFFFFFF:08x}"


def verify_record(row: dict) -> bool:
    return row.get("checksum") == record_checksum(row.get("url", ""), row.get("title", ""))
