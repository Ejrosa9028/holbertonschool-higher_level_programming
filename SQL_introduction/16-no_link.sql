-- Este comando selecciona la puntuación y el nombre de la second_table donde el nombre no es NULL y los ordena por puntuación en orden descendente.
SELECT score, name
FROM second_table
WHERE
    name IS NOT NULL
ORDER BY score DESC;