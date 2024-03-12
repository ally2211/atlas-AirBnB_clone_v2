-- Create the database and user
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'; 

-- Grant the necessary privileges
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;

-- Check the creation of the database and the user's privileges
-- This will produce output which can be captured and verified outside this script

-- Check if the database exists
SELECT DATABASE() AS CurrentDatabase;
SHOW DATABASES LIKE 'hbnb_test_db';

-- Check if the user exists and their privileges
SELECT CONCAT(user, '@', host) AS UserAccount FROM mysql.user WHERE user='hbnb_test' AND host='localhost';
SHOW GRANTS FOR 'hbnb_test'@'localhost';
