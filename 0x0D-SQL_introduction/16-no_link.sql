-- Script that list all records of second_table in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
