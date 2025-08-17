-- Ensure the user is created correctly (without spaces before @'localhost')
CREATE USER IF NOT EXISTS 'user_0d_1' @'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant full privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' @'localhost'
WITH
GRANT OPTION;

-- Apply changes
FLUSH PRIVILEGES;

-- Verify the user exists
SELECT User, Host FROM mysql.user WHERE User = 'user_0d_1';

-- Verify granted privileges
SHOW GRANTS FOR 'user_0d_1' @'localhost';