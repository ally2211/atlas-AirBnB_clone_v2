#!/usr/bin/python3
"""
module documentation:  The tests for State are written independently 
without relying on inheritance from a BaseModel test class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for each test"""
        self.state = State()

    def test_initialization(self):
        """Test initialization of State instance"""
        self.assertIsInstance(self.state, State)
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        s_dict = self.state.to_dict()
        self.assertEqual(s_dict["name"], "")
        self.assertEqual(s_dict["__class__"], "State")


if __name__ == "__main__":
    unittest.main()

