#!/usr/bin/python3
"""
Test cases for base.py
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """
    test_no_input - tests if no id is given to Base class
    test_id_input - tests if one id is given to the Base class
    """
    def test_no_input(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_input(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
