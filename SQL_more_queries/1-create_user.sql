-- Creates 'user_0d_1' on 'localhost' with the password 'user_0d_1_pwd' if they don't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grants all privileges on all databases and tables to 'user_0d_1' on 'localhost
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';