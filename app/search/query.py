"""Parse a user query string into SQL fragments."""
from __future__ import annotations

import re
import shlex

FIELD = re.compile(r"^(tag|site|is):(.+)$")


def parse(raw: str) -> tuple[str, dict[str, list[str]]]:
    terms: list[str] = []
    filters: dict[str, list[str]] = {}
    try:
        tokens = shlex.split(raw)
    except ValueError:
        tokens = raw.split()
    for token in tokens:
        m = FIELD.match(token)
        if m:
            filters.setdefault(m.group(1), []).append(m.group(2))
        else:
            terms.append(token)
    return " ".join(terms), filters
