-- script that lists all the genres from  hbtn_0d_tvshows and displays the number of shows linked to each other
SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id ORDER BY number_of_shows DESC;
