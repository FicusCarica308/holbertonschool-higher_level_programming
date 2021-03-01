-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id WHERE tv_show_genres.show_id = 8 ORDER BY tv_genres.name ASC;
