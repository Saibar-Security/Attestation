CREATE TABLE users (
    id         SERIAL PRIMARY KEY,
    email      TEXT UNIQUE NOT NULL,
    token_sig  TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE bookmarks (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER REFERENCES users(id),
    url        TEXT NOT NULL,
    title      TEXT DEFAULT '',
    note       TEXT DEFAULT '',
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE INDEX bookmarks_user_created_idx ON bookmarks (user_id, created_at DESC);
