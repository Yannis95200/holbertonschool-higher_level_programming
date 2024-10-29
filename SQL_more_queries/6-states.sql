-- Creates the 'hbtn_0d_usa' database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Selects 'hbtn_0d_usa' as the current database
USE hbtn_0d_usa;

-- Creates the 'states' table with:
--   - 'id' (INT, auto-increment, unique, non-null, primary key)
--   - 'name' (VARCHAR up to 256 characters, non-null)
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);