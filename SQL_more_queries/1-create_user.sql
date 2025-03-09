-- Asegúrese de que el usuario se haya creado correctamente (sin espacios antes de @'localhost')
CREATE USER IF NOT EXISTS 'user_0d_1' @'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Otorgar privilegios completos al usuario
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' @'localhost'
WITH
GRANT OPTION;

-- Aplicar cambios
FLUSH PRIVILEGES;

-- Verificar que el usuario existe
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';

-- Verificar privilegios concedidos
SHOW GRANTS FOR 'user_0d_1' @'localhost';