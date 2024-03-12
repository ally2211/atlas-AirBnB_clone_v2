#!/usr/bin/python3
""" Unit tests for State class """
import unittest
from models.state import State
from models.base_model import BaseModel
import os
import datetime


class TestState(unittest.TestCase):

    def setUp(self):
        """Set up for each test"""
        self.state = State()

    def tearDown(self):
        """Tear down for each test"""
        del self.state
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_is_instance(self):
        """Test for instantiation"""
        self.assertTrue(isinstance(self.state, State))
        self.assertTrue(isinstance(self.state, BaseModel))

    def test_attribute_existence(self):
        """Test if attributes exist"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "id"))

    def test_attribute_type(self):
        """Test attribute types"""
        self.assertIsInstance(self.state.name, str)
        self.assertIsInstance(self.state.created_at, datetime.datetime)
        self.assertIsInstance(self.state.updated_at, datetime.datetime)
        self.assertIsInstance(self.state.id, str)

    def test_inherited_methods(self):
        """Test if State has all of BaseModel's methods"""
        self.assertTrue(hasattr(self.state, "save"))
        self.assertTrue(hasattr(self.state, "to_dict"))

    def test_to_dict(self):
        """Test to_dict method"""
        s_dict = self.state.to_dict()
        self.assertEqual(s_dict["name"], self.state.name)
        self.assertEqual(s_dict["__class__"], "State")
        self.assertEqual(s_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(s_dict["updated_at"], self.state.updated_at.isoformat())
        self.assertEqual(s_dict["id"], self.state.id)

    def test_str_representation(self):
        """Test string representation of State"""
        expected = "[{}] ({}) {}".format(self.state.__class__.__name__, self.state.id, self.state.__dict__)
        self.assertEqual(expected, str(self.state))


if __name__ == "__main__":
    unittest.main()
