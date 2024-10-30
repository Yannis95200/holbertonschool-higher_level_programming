-- Selects 'id' and 'name' from 'cities' and 'name' from 'states' by joining the two tables on 'state_id'
-- Orders the results by 'cities.id' in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;