-- Seleccione los títulos de los programas y sus nombres de género correspondientes (o NULL si no hay género)
SELECT tv_shows.title, tv_genres.name
FROM
    tv_shows
    -- Utilice LEFT JOIN para incluir todos los programas, incluso si no tienen género
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Ordenar los resultados por título del programa y luego por nombre de género
ORDER BY tv_shows.title ASC, tv_genres.name ASC;