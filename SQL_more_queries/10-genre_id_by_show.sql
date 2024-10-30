-- Selects 'title' from 'tv_shows' and 'genre_id' from 'tv_show_genres' by joining the two tables on 'id' and 'show_id'
-- Orders the results by 'tv_shows.title' and 'tv_show_genres.genre_id' in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;