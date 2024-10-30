-- Selects the titles of shows from 'tv_shows' and their associated genre names
-- Uses LEFT JOINs to include all shows even if they have no associated genres
-- Orders the results by show title and genre name in ascending order
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;