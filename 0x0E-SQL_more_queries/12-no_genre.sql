-- Lists all shows contained in the hbtn_0d_tvshows database that have no genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
