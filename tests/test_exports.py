import json
import os

from app.bookmarks import bundle
from app.utils.checksum import verify_record

DATA = os.path.join(os.path.dirname(__file__), "data", "exports")


def _load(name, passphrase, salt, iterations):
    with open(os.path.join(DATA, name), "rb") as fh:
        blob = fh.read()
    key = bundle.derive_key(passphrase, salt, iterations)
    return [json.loads(line) for line in bundle.unpack(blob, key).splitlines() if line]


def test_legacy_bundle_round_trips():
    rows = _load(
        "bundle_2021_11_02.lkb",
        os.environ["SECRET_KEY"],
        "9c1f4a7d2e6b08f35a9d4c7e1b02f68a",
        120000,
    )
    assert len(rows) == 96
    assert all(verify_record(r) for r in rows)
