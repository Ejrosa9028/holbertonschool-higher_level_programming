-- Crea la base de datos si no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crea el usuario si no existe.
CREATE USER IF NOT EXISTS 'user_0d_2' @'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Otorgar privilegio SELECT en hbtn_0d_2 a user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2' @'localhost';

-- Aplicar cambios
FLUSH PRIVILEGES;