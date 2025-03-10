-- Seleccione el título del programa de TV y la identificación del género (NULL para programas sin género)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
    -- Utilice LEFT JOIN para conservar todos los programas, incluso aquellos sin géneros
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Filtrar para incluir solo programas donde genre_id es NULL (sin género vinculado)
WHERE
    tv_show_genres.genre_id IS NULL
    -- Ordenar los resultados por título del programa de TV en orden ascendente
ORDER BY tv_shows.title ASC;