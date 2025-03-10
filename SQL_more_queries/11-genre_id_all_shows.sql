-- Seleccione el título del programa de TV y la identificación del género (se permite NULL para programas sin género)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Realizar una LEFT JOIN (UNIÓN IZQUIERDA) para incluir programas incluso si no tienen género
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Ordenar los resultados en orden ascendente por título del programa de TV e ID de género
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;