ALTER TABLE bookmarks ADD COLUMN search_vector tsvector;
CREATE INDEX bookmarks_search_idx ON bookmarks USING GIN (search_vector);
