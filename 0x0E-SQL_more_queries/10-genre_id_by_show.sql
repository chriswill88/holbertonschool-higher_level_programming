-- genre id by show
SELECT title, genre_id FROM tv_shows JOIN tv_show_genres WHERE tv_shows.id = show_id ORDER BY title ASC, genre_id ASC;
