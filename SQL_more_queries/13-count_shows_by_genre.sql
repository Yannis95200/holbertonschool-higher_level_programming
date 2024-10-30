-- Selects 'name' from 'tv_genres' as 'genre' and counts the number of shows for each genre
-- Joins 'tv_genres' with 'tv_show_genres' on 'id' and 'genre_id', groups by genre ID
-- Orders the results by 'number_of_shows' in descending order
SELECT tv_genres.name AS genre, COUNT(tv_genres.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;