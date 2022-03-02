import responses

from app.integrations.wallabag import BASE_URL, WallabagClient


@responses.activate
def test_iter_items_paginates():
    responses.add(
        responses.GET,
        f"{BASE_URL}/items",
        json={"items": [{"url": "https://example.com", "title": "Example"}],
              "next_cursor": None},
    )
    client = WallabagClient("tok")
    assert len(list(client.iter_items())) == 1


@responses.activate
def test_normalise_prefers_url_over_link():
    client = WallabagClient("tok")
    bm = client.normalise({"url": "https://a.example", "link": "https://b.example",
                           "title": " Spaced "})
    assert bm.url == "https://a.example"
    assert bm.title == "Spaced"
