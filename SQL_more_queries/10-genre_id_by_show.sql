-- Seleccione el título del programa de TV y el ID del género
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Realizar una UNIÓN INTERNA para vincular tv_shows con tv_show_genres
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Ordenar los resultados en orden ascendente por título del programa de TV e ID de género
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;