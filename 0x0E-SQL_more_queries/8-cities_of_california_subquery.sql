-- Displays all cities that are in California
SELECT id, name
FROM cities
WHERE state_id =
    (SELECT id
     FROM states
     WHERE name = "California");
