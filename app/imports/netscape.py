"""Parse the Netscape bookmark-file format every browser still exports."""
from __future__ import annotations

import html.parser


class _Parser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.items: list[dict] = []
        self._href: str | None = None
        self._add_date: str = ""

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        attrs = dict(attrs)
        self._href = attrs.get("href")
        self._add_date = attrs.get("add_date", "")

    def handle_data(self, data):
        if self._href:
            self.items.append(
                {"url": self._href, "title": data.strip(), "added": self._add_date}
            )
            self._href = None


def parse(markup: str) -> list[dict]:
    p = _Parser()
    p.feed(markup)
    return p.items
