-- a script that creates the MySQL server user user_0d_1 with all permissions
-- password is set to user_0d_1_pwd
-- creates only if user doesnt exist !
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost'
FLUSH PRIVILEGES;
