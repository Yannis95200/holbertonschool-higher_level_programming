-- Selects the names of genres from 'tv_genres' for the show 'Dexter'
-- Joins 'tv_genres' with 'tv_show_genres' and 'tv_shows' to filter by show title
-- Orders the results by genre name in ascending orde
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;