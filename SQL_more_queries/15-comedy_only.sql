-- Seleccione títulos de programas que pertenezcan al género "Comedy"
SELECT tv_shows.title
FROM
    tv_shows
    -- Únase a tv_show_genres para obtener relaciones entre programas y géneros
    INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    -- Únete a tv_genres para filtrar solo el género "Comedy"
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    -- Asegúrese de seleccionar solo los programas categorizados como "Comedy"
WHERE
    tv_genres.name = 'Comedy'
    -- Ordenar resultados por título de visualización en orden ascendente
ORDER BY tv_shows.title ASC;