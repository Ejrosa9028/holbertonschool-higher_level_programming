-- Seleccione los nombres de los géneros vinculados al programa "Dexter"
SELECT tv_genres.name
FROM
    tv_genres
    -- Únase a tv_show_genres para obtener relaciones de género
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Únete a tv_shows para filtrar solo el programa "Dexter"
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    -- Asegúrese de seleccionar solo el programa con el título "Dexter"
WHERE
    tv_shows.title = 'Dexter'
    -- Ordenar géneros en orden ascendente
ORDER BY tv_genres.name ASC;