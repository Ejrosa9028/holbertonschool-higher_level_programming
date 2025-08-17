-- Select show titles and their corresponding genre names (or NULL if no genre)
SELECT tv_shows.title, tv_genres.name
FROM
    tv_shows
    -- Use LEFT JOIN to include all shows, even if they have no genre
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Sort results by show title and then by genre name
ORDER BY tv_shows.title ASC, tv_genres.name ASC;