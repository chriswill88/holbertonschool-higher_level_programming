-- gets average temps limit 3
SELECT city, AVG(value) AS avg_temp FROM hbtn_0c_0.temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
