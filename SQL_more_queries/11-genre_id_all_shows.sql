-- Select TV show title and genre ID (allowing NULL for shows with no genre)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Perform a LEFT JOIN to include shows even if they have no genre
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Sort results in ascending order by TV show title and genre ID
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;