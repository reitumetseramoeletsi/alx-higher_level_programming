-- Script that lists all cities of Carlifonia
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name='California')
ORDER BY cities.id ASC;
