CREATE TABLE books (
  id INTEGER,
  title TEXT,
  author TEXT
);
-- Do not modify above this line --

-- add new col
ALTER TABLE books ADD COLUMN published_year INTEGER;
-- rename col id > isbn
ALTER TABLE books RENAME COLUMN id TO isbn;
-- drop author col
ALTER TABLE books DROP COLUMN author;









-- Do not modify below this line --
SELECT column_name, data_type, column_default
FROM information_schema.columns
WHERE table_name = 'books'
ORDER BY column_name;
