#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer([])"""
    def test_empty_list(self):
        """To test if the list is empty"""
        empty_list = []
        self.assertEqual(max_integer(empty), None)

    def test_order_valid(self):
        """to assert if it is a valid list"""
        self.assertEqual(max_integer([1, 2, 3, 4], 4)
        self.assertEqual(max_integer([1, 3, 4, 2]),4)

    def test_unordered(self):
        self.assertEqual(max_integer(unordered), 4)

    def test_max_beg(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_onlyOne_arg(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_elements(self):
        self.assertEqual(max_integer([1, -1, 0, -2]), 1)

    def test_object_type(self):
        self.assertIs(list, list)

    def test_exists_two_max(self):
        self.assertEqual(max_integer([3, 3, 1, 2]), 3)

    def test_floats(self):
        self.assetEqual(max_integer([0.0, 3.1, 3, 2.1]), 3.1)

    def test_raises(self):
        self.assertRaises(TypeError, max_integer, [1, "him", 4], mesg="unorderable types: str() > int()")
	self.assertRaises(TypeError,max_integer, [2, 4, '5'], msg="unorderable types: str() > int()")
