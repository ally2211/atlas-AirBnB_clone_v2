#!/usr/bin/python3
"""module for testing the BaseModel class."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up the test case environment"""
        self.hbnb_cmd = HBNBCommand()
        self.hbnb_cmd.stdout = StringIO()  # Redirect stdout to capture print statements

    def tearDown(self):
        """Clean up the test case environment"""
        self.hbnb_cmd.stdout.close()
        del self.hbnb_cmd

    def test_quit(self):
        """Test the quit command"""
        with self.assertRaises(SystemExit):
            self.hbnb_cmd.onecmd("quit")
        self.assertEqual(self.hbnb_cmd.stdout.getvalue(), '')

    def test_EOF(self):
        """Test the EOF command"""
        with self.assertRaises(SystemExit):
            self.hbnb_cmd.onecmd("EOF")
        self.assertEqual(self.hbnb_cmd.stdout.getvalue(), '\n')

    def test_create_missing_class_name(self):
        """Test the create command with missing class name"""
        self.hbnb_cmd.onecmd("create")
        self.assertEqual(self.hbnb_cmd.stdout.getvalue(), "** class name missing **\n")

    # You can continue to add more tests for other commands and scenarios

if __name__ == "__main__":
    unittest.main()

