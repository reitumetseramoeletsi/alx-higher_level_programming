-- Script that lists the number of records that have the same score in secon_table
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score ORDER BY score DESC 
