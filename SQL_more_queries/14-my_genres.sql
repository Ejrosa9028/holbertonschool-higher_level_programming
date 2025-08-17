-- Select genre names linked to the show "Dexter"
SELECT tv_genres.name
FROM
    tv_genres
    -- Join with tv_show_genres to get genre relationships
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Join with tv_shows to filter only the show "Dexter"
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    -- Ensure we select only the show with title "Dexter"
WHERE
    tv_shows.title = 'Dexter'
    -- Sort genres in ascending order
ORDER BY tv_genres.name ASC;