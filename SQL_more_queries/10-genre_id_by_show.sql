-- Select the TV show title and genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Perform an INNER JOIN to link tv_shows with tv_show_genres
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Sort results in ascending order by TV show title and genre ID
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;