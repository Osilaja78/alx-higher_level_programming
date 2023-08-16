#!/usr/bin/python3
"""
Unittest for Square module.
"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """To test the Square module"""

    def test_constructor(self):
        s = Square(5, 1, 2, 3)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 3)

    def test_update_args(self):
        s = Square(5, 1, 2, 3)
        s.update(4, 10, 3, 4)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        s = Square(5, 1, 2, 3)
        s.update(size=10, x=3, y=4)
        self.assertEqual(s.size, 10)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 3)
        expected_dict = {'id': 3, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_str(self):
        s = Square(5, 1, 2, 3)
        expected_str = "[Square] (3) 1/2 - 5"
        self.assertEqual(str(s), expected_str)


class TestSquareGeterAndSetter(unittest.TestCase):
    """Test for Square getter and setter methods"""

    def test_size_getter_and_setter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        with self.assertRaises(TypeError):
            s.size = "test"
        with self.assertRaises(TypeError):
            s.size = False
        with self.assertRaises(ValueError):
            s.size = -5
        with self.assertRaises(ValueError):
            s.size = 0


if __name__ == "__main__":
    unittest.main()
