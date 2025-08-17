-- Select show titles that belong to the "Comedy" genre
SELECT tv_shows.title
FROM
    tv_shows
    -- Join tv_show_genres to get show-genre relationships
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Join tv_genres to filter only the genre "Comedy"
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Ensure we select only the shows categorized as "Comedy"
WHERE
    tv_genres.name = 'Comedy'
    -- Sort results by show title in ascending order
ORDER BY tv_shows.title ASC;