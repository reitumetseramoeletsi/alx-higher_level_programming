-- Script that displays the top 3 cities temperatures during July and August
-- in descending order
SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month IN (7, 8)
GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
