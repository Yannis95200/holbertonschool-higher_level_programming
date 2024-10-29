-- Creates the database 'hbtn_0d_2' if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates 'user_0d_2' on 'localhost' with the password 'user_0d_2_pwd' if they don't already exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grants SELECT privilege on all tables in the 'hbtn_0d_2' database to 'user_0d_2' on 'localhost
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';