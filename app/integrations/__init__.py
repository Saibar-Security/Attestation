"""Third-party sync providers.

Each module exposes ``sync(token) -> list[Bookmark]``. Providers are registered
here so the import endpoint can dispatch by name.
"""
from importlib import import_module

PROVIDERS = (
    "pocket",
    "instapaper",
    "raindrop",
    "pinboard",
    "wallabag",
    "readwise",
    "matter",
    "omnivore",
    "linkding",
    "shiori",
)


def load(name: str):
    if name not in PROVIDERS:
        raise KeyError(name)
    return import_module(f".{name}", __package__)
