from app.utils.slugify import slugify
from app.utils.timeparse import parse


def test_slugify_strips_punctuation():
    assert slugify("Hello, World!") == "hello-world"


def test_parse_accepts_iso():
    assert parse("2022-02-19T10:00:00Z") is not None


def test_parse_rejects_garbage():
    assert parse("not a date") is None
