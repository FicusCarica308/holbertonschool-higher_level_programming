#!/usr/bin/python3
"""
Test cases for square.py
"""
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.base import Base
from models.square import Square


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
        sqr = Square(10, 3, 4, 12)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.height, 10)
        self.assertEqual(sqr.x, 3)
        self.assertEqual(sqr.y, 4)
        self.assertEqual(sqr.id, 12)

    def test_setters(self):
        """ Tests setters """
        sqr = Square(10, 3, 4, 12)
        # ---SIZE---
        sqr.size = 24
        self.assertEqual(sqr.size, 24)
        self.assertEqual(sqr.height, 24)
        self.assertEqual(sqr.width, 24)
        # ---X---
        sqr.x = 5
        self.assertEqual(sqr.x, 5)
        # ---Y---
        sqr.y = 6
        self.assertEqual(sqr.y, 6)
        # ---ID ---
        sqr.id = 127
        self.assertEqual(sqr.id, 127)

    def test_value_errors(self):
        """ Tests value errors """
        sqr = Square(10, 3, 4, 12)
        # -----size--------width/height
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sqr.size = -10
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sqr.x = -10
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sqr.y = -30

    def test_type_errors(self):
        """ Tests Type errors """
        sqr = Square(10, 3, 4, 12)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.size = dict()
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.size = list()
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.x = str()
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.y = list()
        # ---- None -----
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.size = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sqr.size = None
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sqr.x = None
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sqr.y = None

    def test_area(self):
        """ Tests area method """
        sqr = Square(10, 3, 4)
        self.assertEqual(sqr.area(), 100)
        sqr = Square(30, 10, 3, 4)
        self.assertEqual(sqr.area(), 900)

    def test_print(self):
        """ Tests print method """
        expected = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(2)
            s1.display()
        self.assertEqual(fake_out.getvalue(), expected)

        expected = "\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            s1 = Square(2, 1, 1)
            s1.display()
        self.assertEqual(fake_out.getvalue(), expected)

    def test_str_out(self):
        """ Tests str print() method """
        s1 = Square(4)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 4")

    def test_to_dict(self):
        """ Tests todict() method """
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        test_dict = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(s1_dictionary, test_dict)

    def test_update(self):
        """ Tests update method """
        # -----ARGS--------
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(str(s1), "[Square] (10) 10/10 - 10")
        s1.update(89)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 10")
        s1.update(89, 2)
        self.assertEqual(str(s1), "[Square] (89) 10/10 - 2")
        s1.update(89, 2, 3)
        self.assertEqual(str(s1), "[Square] (89) 3/10 - 2")
        s1.update(89, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (89) 3/4 - 2")
        # -------KWARGS------
        s2 = Square(10, 10, 10, 10)
        self.assertEqual(str(s2), "[Square] (10) 10/10 - 10")
        s2.update(size=1)
        self.assertEqual(str(s2), "[Square] (10) 10/10 - 1")
        s2.update(size=1, x=2)
        self.assertEqual(str(s2), "[Square] (10) 2/10 - 1")
        s2.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(s2), "[Square] (89) 3/1 - 2")
        s2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(s2), "[Square] (89) 1/3 - 4")
