-- Este comando crea una tabla llamada second_table si no existe
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- Este comando inserta varias filas en la second_table
INSERT INTO
    second_table (id, name, score)
VALUES (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);