-- Select genre name and count of linked TV shows
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
    -- Join tv_show_genres to count shows per genre
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Group by genre name to count the number of associated shows
GROUP BY
    tv_genres.name
    -- Sort by number_of_shows in descending order
ORDER BY number_of_shows DESC;