#!/usr/bin/python3
import unittest
from console import HBNBCommand
from io import StringIO
import sys


class TestConsole(unittest.TestCase):

    def setUp(self):
        """Set up for each test"""
        self.console = HBNBCommand()

    def test_create_command(self):
        """Test create command"""
        sys.stdout = StringIO()  # Capture stdout
        self.console.onecmd('create State name="California"')
        output = sys.stdout.getvalue().strip()
        self.assertIn("State", output)  # You can customize this test based on expected output
        sys.stdout = sys.__stdout__  # Reset stdout

    # Add more tests for other commands


if __name__ == "__main__":
    unittest.main()

