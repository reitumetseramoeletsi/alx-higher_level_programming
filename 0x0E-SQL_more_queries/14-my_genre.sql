-- Script that lists all genres of the show Dexter using hbtn
SELECT a.name FROM tv_genres a JOIN tv_show_genres b ON a.id = b.genre_id
JOIN tv_shows c ON c.id = b.show_id WHERE c.title = 'Dexter' ORDER BY a.name ASC;
