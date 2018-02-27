-- Counts how many students got the same scores
SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score DESC;
