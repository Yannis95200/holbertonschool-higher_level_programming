-- Retrieves 'score' and 'name' from 'second_table' where 'name' is not null, ordered by 'score' in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;