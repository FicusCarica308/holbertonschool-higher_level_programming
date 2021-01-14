#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        self.assertAlmostEqual(max_integer([1, 4, 5]), 5)
    def test_mex_start(self):
        self.assertAlmostEqual(max_integer([5, 4, 3]), 5)
    def test_max_middle(self):
        self.assertAlmostEqual(max_integer([1, 2, 25, 4, 5]), 25)
    def test_neg(self):
        self.assertAlmostEqual(max_integer([1, 2, -23, 4, 5]), 5)
    def test_all_neg(self):
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4, -5]), -1)
    def test_one_ele(self):
        self.assertAlmostEqual(max_integer([-1]), -1)
    def test_empty(self):
        self.assertAlmostEqual(max_integer([]), None)