-- Creates the 'unique_id' table with 'id' (INT, unique with a default value of 1) and 'name' (VARCHAR up to 256 characters)
CREATE TABLE unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));