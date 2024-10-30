-- Creates the 'hbtn_0d_usa' database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects 'hbtn_0d_usa' as the current database
USE hbtn_0d_usa;

-- Creates the 'cities' table with:
--   - 'id' (INT, auto-increment, unique, non-null, primary key)
--   - 'state_id' (INT, non-null, foreign key referencing 'id' in 'states' table)
--   - 'name' (VARCHAR up to 256 characters)
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
