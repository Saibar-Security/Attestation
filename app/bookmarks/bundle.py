"""Portable, encrypted export bundles.

A bundle is a single file a user can download, keep, and re-import later or
somewhere else. It is encrypted with a key derived from the deployment secret
and a per-profile salt, so a bundle taken off a backup disk is not readable
without knowing which deployment produced it.

Container layout::

    offset  0   4   magic        b"LKB1"
    offset  4   1   version      currently 1
    offset  5   1   profile_id   FK -> export_profiles.id
    offset  6   2   reserved     zero
    offset  8   4   length       payload length, big-endian
    offset 12   n   payload      NDJSON XOR keystream

The key is PBKDF2-HMAC-SHA256 over the deployment secret with the profile's
salt and iteration count. The keystream is the concatenation of
``sha256(key || counter)`` for counter = 0, 1, 2, ... as 4-byte big-endian
integers, which keeps the reader dependency-free.
"""
from __future__ import annotations

import hashlib

MAGIC = b"LKB1"
VERSION = 1
HEADER_LEN = 12


def derive_key(passphrase: str, salt_hex: str, iterations: int) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256", passphrase.encode(), bytes.fromhex(salt_hex), iterations, dklen=32
    )


def keystream(key: bytes, n: int) -> bytes:
    out = bytearray()
    counter = 0
    while len(out) < n:
        out += hashlib.sha256(key + counter.to_bytes(4, "big")).digest()
        counter += 1
    return bytes(out[:n])


def profile_id(blob: bytes) -> int:
    """Read the export profile a bundle was written with, without the key."""
    if blob[:4] != MAGIC:
        raise ValueError("not a Larkspur bundle")
    return blob[5]


def pack(payload: bytes, pid: int, key: bytes) -> bytes:
    header = MAGIC + bytes([VERSION, pid, 0, 0]) + len(payload).to_bytes(4, "big")
    return header + bytes(a ^ b for a, b in zip(payload, keystream(key, len(payload))))


def unpack(blob: bytes, key: bytes) -> bytes:
    if blob[:4] != MAGIC:
        raise ValueError("not a Larkspur bundle")
    n = int.from_bytes(blob[8:12], "big")
    body = blob[HEADER_LEN : HEADER_LEN + n]
    return bytes(a ^ b for a, b in zip(body, keystream(key, n)))
