-- script that lists all shows with at least 1 genre
-- query to select the shows form the database

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows_genre ON tv_shows.id = tv_shows_genre.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id; 
