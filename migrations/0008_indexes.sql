CREATE INDEX bookmarks_url_idx ON bookmarks (url);
CREATE INDEX feeds_user_idx ON feeds (user_id);
ANALYZE bookmarks;
