-- dont list rows without a name,
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY SCORE DESC;
