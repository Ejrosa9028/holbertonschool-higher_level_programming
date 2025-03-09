-- Seleccione los campos obligatorios: ID de ciudad, nombre de la ciudad y nombre del estado
SELECT cities.id, cities.name, states.name
FROM cities
    -- Realizar una INNER JOIN (UNION INTERNA) para unir ciudades con sus estados correspondientes
    INNER JOIN states ON cities.state_id = states.id
    -- Ordenar los resultados por ID de ciudad en orden ascendente
ORDER BY cities.id ASC;