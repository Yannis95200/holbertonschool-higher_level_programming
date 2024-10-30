-- Selects the titles of shows from 'tv_shows' that belong to the 'Comedy' genre
-- Joins 'tv_shows' with 'tv_show_genres' and 'tv_genres' to filter by genre name
-- Orders the results by show title in ascending order
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;