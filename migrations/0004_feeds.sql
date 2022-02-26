CREATE TABLE feeds (
    id          SERIAL PRIMARY KEY,
    user_id     INTEGER REFERENCES users(id),
    url         TEXT NOT NULL,
    title       TEXT DEFAULT '',
    etag        TEXT DEFAULT '',
    last_polled TIMESTAMPTZ
);
