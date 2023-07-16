#!/usr/bin/python3
"""
Unittest for Base.
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    Test for Base model.
    """

    def test_id(self):
        base_1 = Base()
        base_2 = Base()
        base_3 = Base()
        base_4 = Base(14)
        base_5 = Base(12)
        base_6 = Base()
        base_7 = Base(-3)

        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)
        self.assertEqual(base_3.id, 3)
        self.assertEqual(base_4.id, 14)
        self.assertEqual(base_5.id, 12)
        self.assertEqual(base_6.id, 4)
        self.assertEqual(base_7.id, -3)
    
if __name__ == "__main__":
    unittest.main()