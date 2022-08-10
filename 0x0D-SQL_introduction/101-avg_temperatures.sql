-- Script that displays the temparatures of a city in Fahrenheit orederd in descend-- ing order
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
