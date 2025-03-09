-- Crear base de datos si no existe hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilice la base de datos creada o existente
USE hbtn_0d_usa;

-- Crear tabla si no existe states
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);