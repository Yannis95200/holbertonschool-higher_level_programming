-- Selects 'id' and 'name' from 'cities' where 'state_id' matches the 'id' of the state named 'California' in 'states'
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
