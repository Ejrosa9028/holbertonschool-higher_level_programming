-- Este comando agrupa las puntuaciones en la second_table y cuenta el número de ocurrencias de cada puntuación.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY
    score
ORDER BY number DESC;