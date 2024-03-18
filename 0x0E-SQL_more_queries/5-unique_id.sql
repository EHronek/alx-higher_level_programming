-- creates a table unique_id on mysql server and should not fail if it exists
-- id INT with default value 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1 NOT NULL, name VARCHAR(256));
