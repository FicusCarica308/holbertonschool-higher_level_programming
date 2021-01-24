#!/usr/bin/python3
"""
Test cases for rectangle.py
"""
import unittest
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """
    test_no_input - tests if no id is given to Base class
    test_id_input - tests if one id is given to the Base class
    """
    def test_getters(self):
        rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 12)
