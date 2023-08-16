#!/usr/bin/python3
"""
Unittest for Rectangle.
"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest import mock


class TestRectangle(unittest.TestCase):
    """Test for Rectangle model"""

    def test_constructor(self):
        r = Rectangle(5, 10, 1, 2, 3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_area(self):
        r1 = Rectangle(5, 10)
        r2 = Rectangle(3, 5)

        self.assertEqual(r1.area(), 50)
        self.assertEqual(r2.area(), 15)

    def test_display(self):
        r = Rectangle(5, 5)
        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            r.display()
            output = fake_out.getvalue()
            self.assertEqual(output, "#####\n#####\n#####\n#####\n#####\n")

    def test_str(self):
        r1 = Rectangle(5, 10, 1, 2, 3)
        expected_str = "[Rectangle] (3) 1/2 - 5/10"
        self.assertEqual(str(r1), expected_str)

    def test_update_args(self):
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(4, 15, 20, 3, 4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_update_kwargs(self):
        r = Rectangle(5, 10, 1, 2, 3)
        r.update(width=15, height=20, x=3, y=4)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2, 3)
        expected_dict = {'id': 3, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)


class TestRectangleSetterAndGetter(unittest.TestCase):
    """To test getter and setter methods"""

    def test_width_getter_and_setter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(TypeError):
            r.width = "test"
        with self.assertRaises(TypeError):
            r.width = True
        with self.assertRaises(ValueError):
            r.width = -5
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_getter_and_setter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.height, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

        with self.assertRaises(TypeError):
            r.height = "test"
        with self.assertRaises(TypeError):
            r.height = True
        with self.assertRaises(ValueError):
            r.height = -5
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_getter_and_setter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.x, 0)
        r.x = 3
        self.assertEqual(r.x, 3)
        with self.assertRaises(TypeError):
            r.x = "test"
        with self.assertRaises(TypeError):
            r.x = True
        with self.assertRaises(ValueError):
            r.x = -5

    def test_y_getter_and_setter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.y, 0)
        r.y = 4
        self.assertEqual(r.y, 4)
        with self.assertRaises(TypeError):
            r.y = "test"
        with self.assertRaises(TypeError):
            r.y = True
        with self.assertRaises(ValueError):
            r.y = -5
