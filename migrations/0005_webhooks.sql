CREATE TABLE webhooks (
    id         SERIAL PRIMARY KEY,
    user_id    INTEGER REFERENCES users(id),
    endpoint   TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT now()
);
