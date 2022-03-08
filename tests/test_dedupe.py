from app.bookmarks.dedupe import canonical


def test_strips_tracking_params():
    assert canonical("https://a.example/x?utm_source=n&id=2") == "https://a.example/x?id=2"


def test_lowercases_host_and_trims_path():
    assert canonical("https://A.Example/x/") == "https://a.example/x"
