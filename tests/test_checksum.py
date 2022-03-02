from app.utils.checksum import record_checksum, verify_record


def test_checksum_is_stable():
    assert record_checksum("https://example.com", "Example") == record_checksum(
        "https://example.com", "Example"
    )


def test_checksum_covers_title():
    a = record_checksum("https://example.com", "One")
    b = record_checksum("https://example.com", "Two")
    assert a != b


def test_verify_record_round_trip():
    row = {"url": "https://example.com", "title": "Example"}
    row["checksum"] = record_checksum(row["url"], row["title"])
    assert verify_record(row)
