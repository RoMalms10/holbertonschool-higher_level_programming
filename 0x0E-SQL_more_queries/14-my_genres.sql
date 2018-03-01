-- Shows which genres are tagged for Dexter
SELECT tv_genres.name AS name
FROM tv_show_genres
LEFT OUTER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id =
    (SELECT id
     FROM tv_shows
     WHERE title = "Dexter")
ORDER BY name ASC;
