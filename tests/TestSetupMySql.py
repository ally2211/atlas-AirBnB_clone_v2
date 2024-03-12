#!/usr/bin/python3
"""module for testing the SQL DB connection."""

import unittest
import MySQLdb

class TestMySQLScript(unittest.TestCase):
    """Class for testing the SQL DB connection."""
    def setUp(self):
        # Connect to the MySQL database. Adjust these parameters.
        self.db = MySQLdb.connect(host="localhost", user="root", password="root")
        self.cursor = self.db.cursor()

        # Execute the provided SQL script
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS hbnb_dev_db;")
        self.cursor.execute("CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';")
        self.cursor.execute("GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';")
        self.cursor.execute("GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';")
        self.cursor.execute("FLUSH PRIVILEGES;")

    def test_database_exists(self):
        self.cursor.execute("SHOW DATABASES LIKE 'hbnb_dev_db';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_user_exists(self):
        self.cursor.execute("SELECT user, host FROM mysql.user WHERE user='hbnb_dev' AND host='localhost';")
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)

    def test_user_has_permissions(self):
        # Test SELECT permission on performance_schema
        self.cursor.execute("SHOW GRANTS FOR 'hbnb_dev'@'localhost';")
        grants = self.cursor.fetchall()
        self.assertIn(('GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`',), grants)
        # Test ALL privileges on hbnb_dev_db
        self.assertIn(('GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO `hbnb_dev`@`localhost`',), grants)

    def tearDown(self):
        # Cleanup (optional, but good practice)
        self.cursor.execute("DROP DATABASE IF EXISTS hbnb_dev_db;")
        self.cursor.execute("DROP USER 'hbnb_dev'@'localhost';")
        self.cursor.close()
        self.db.close()

if __name__ == "__main__":
    unittest.main()

