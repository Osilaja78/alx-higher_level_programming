#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer(()))
        self.assertIsNone(max_integer(''))

    def test_list_type(self):
        self.assertRaises(TypeError, max_integer, 7)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, {2, 4})

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer('b'), 'b')

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 1, 4, 4]), 4)
        self.assertEqual(max_integer([1, 3, 3, 5, 4, 4, 4]), 5)

    def test_mixed_elements(self):
        self.assertRaises(TypeError, max_integer, [7, 'b'])
        self.assertEqual(max_integer([5, 0.3, 1.2, 4]), 5)
        self.assertEqual(max_integer([-1, -5, False]), False)
        self.assertEqual(max_integer([5, .544, True]), 5)

    def test_zero(self):
        self.assertEqual(max_integer([0, -1, 2, -3, 4, -5]), 4)

if __name__ == "__main__":
    unittest.main()
