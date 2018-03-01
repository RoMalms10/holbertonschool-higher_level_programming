-- Shows which genres are tagged for Dexter
SELECT tv_genres.name AS name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE title = "Dexter"
ORDER BY name ASC;
