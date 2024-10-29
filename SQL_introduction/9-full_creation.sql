-- Creates 'second_table' if it doesn't exist with columns 'id', 'name', and 'score'
CREATE TABLE IF NOT EXISTS second_table (
    id int,
    name VARCHAR(256),
    score INT
);

-- Inserts multiple records into 'second_table'
INSERT INTO second_table(id, name, score)
VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);