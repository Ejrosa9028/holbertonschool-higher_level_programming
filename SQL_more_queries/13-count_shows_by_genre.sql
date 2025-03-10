-- Seleccione el nombre del género y la cantidad de programas de TV vinculados
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
    -- Únase a tv_show_genres para contar programas por género
    INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    -- Agrupar por nombre de género para contar la cantidad de programas asociados
GROUP BY
    tv_genres.name
    -- Ordenar por número de presentaciones en orden descendente
ORDER BY number_of_shows DESC;