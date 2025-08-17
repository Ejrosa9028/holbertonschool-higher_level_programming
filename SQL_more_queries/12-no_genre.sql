-- Select TV show title and genre ID (NULL for shows with no genre)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Use LEFT JOIN to keep all shows, even those without genres
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Filter to only include shows where genre_id is NULL (no genre linked)
WHERE
    tv_show_genres.genre_id IS NULL
    -- Sort results by TV show title in ascending order
ORDER BY tv_shows.title ASC;