#!/usr/bin/python3
"""
Test cases for rectangle.py
"""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """
    test_no_input - tests if no id is given to Base class
    test_id_input - tests if one id is given to the Base class
    """
    def setUp(self):
        """ init's nb_objects """
        Base._Base__nb_objects = 0

    def test_getters(self):
        """ Tests getters """
        rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 12)

    def test_setters(self):
        """ Tests setters """
        rect = Rectangle(10, 2, 3, 4, 12)
        # ---Width ---
        rect.width = 24
        self.assertEqual(rect.width, 24)
        # ---Height ---
        rect.height = 36
        self.assertEqual(rect.height, 36)
        # ---X---
        rect.x = 5
        self.assertEqual(rect.x, 5)
        # ---Y---
        rect.y = 6
        self.assertEqual(rect.y, 6)
        # ---ID ---
        rect.id = 127
        self.assertEqual(rect.id, 127)

    def test_value_errors(self):
        """ Tests value errors """
        rect = Rectangle(10, 2, 3, 4, 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.width = -10
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.height = -25
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect.width = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect.x = -10
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect.y = -30

    def test_type_errors(self):
        """ Tests Type errors """
        rect = Rectangle(10, 2, 3, 4, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.width = dict()
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.height = list()
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.x = str()
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.y = list()
        # ---- None -----
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect.width = None
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect.height = None
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect.x = None
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect.y = None

    def test_area(self):
        """ Tests area method """
        rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(rect.area(), 20)
        rect = Rectangle(30, 10, 3, 4, 12)
        self.assertEqual(rect.area(), 300)

    def test_print(self):
        """ Tests print method """
        r1 = Rectangle(4, 6, 3, 4, 12)
        expected = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6)
            r1.display()
        self.assertEqual(fake_out.getvalue(), expected)

        expected = "\n ####\n ####\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1 = Rectangle(4, 6, 1, 1)
            r1.display()
        self.assertEqual(fake_out.getvalue(), expected)

    def test_str_out(self):
        """ Tests str print() method """
        expected_out = "[Rectangle] (12) 2/1 - 4/6"
        rect = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rect), "[Rectangle] (12) 2/1 - 4/6")

    def test_to_dict(self):
        """ Tests todict() method """
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        test_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertDictEqual(r1_dictionary, test_dict)

    def test_update(self):
        """ Tests update method """
        # -----ARGS--------
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
        # -------KWARGS------
        r2 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 10/10 - 10/10")
        r2.update(height=1)
        self.assertEqual(str(r2), "[Rectangle] (1) 10/10 - 10/1")
        r2.update(width=1, x=2)
        self.assertEqual(str(r2), "[Rectangle] (1) 2/10 - 1/1")
        r2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r2), "[Rectangle] (89) 3/1 - 2/1")
        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r2), "[Rectangle] (89) 1/3 - 4/2")
