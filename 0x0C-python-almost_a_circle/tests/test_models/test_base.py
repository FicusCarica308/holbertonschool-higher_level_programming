#!/usr/bin/python3
"""
Test cases for base.py
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """
    test_no_input - tests if no id is given to Base class
    test_id_input - tests if one id is given to the Base class
    """
    def setUp(self):
        """ init's nb_objects """
        Base._Base__nb_objects = 0

    def test_no_input(self):
        """[summary]
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_input(self):
        """[summary]
        """
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_dict_json_rect(self):
        """[summary]
        """
        # Normal ---------------------
        list_dicts = list()
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        list_dicts.append(dictionary)
        json_check = json.dumps(list_dicts)
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, json_check)
        # None or Empty
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_dict_json_sqr(self):
        """[summary]
        """
        list_dicts = list()
        s1 = Rectangle(10, 7, 2, 8)
        dictionary = s1.to_dictionary()
        list_dicts.append(dictionary)
        json_check = json.dumps(list_dicts)
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, json_check)
        # None or Empty
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

    def test_json_to_file_rect(self):
        """[summary]
        """
        list_dicts = list()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_dicts.append(r1.to_dictionary())
        list_dicts.append(r2.to_dictionary())
        json_check = json.dumps(list_dicts)
        with open("Rectangle.json", "r") as file:
            test = file.read()
        self.assertEqual(test, json_check)

    def test_json_to_dict(self):
        """[summary]
        """
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(type(list_output), list)
        for i in list_output:
            self.assertEqual(type(i), dict)

    def test_dict_to_inst(self):
        """[summary]
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
