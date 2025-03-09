-- Crear base de datos si no existe hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilice la base de datos creada o existente
USE hbtn_0d_usa;

-- Crea los estados de la tabla si no existe (necesario para la clave externa)
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Crea la tabla ciudades si no existe
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states (id) ON DELETE CASCADE
);