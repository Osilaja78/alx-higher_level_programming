#!/usr/bin/python3
"""
Unittest for Base.
"""
import unittest
import json
import csv
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test for Base model.
    """

    @classmethod
    def tearDown(self):
        """tearDown method to delete created files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

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

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(
            Base.to_json_string(
                [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
            ),
            '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        )

    def test_save_to_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        s1 = Square(12, 3, 2, 1)
        s2 = Square(9, 4, 2, 1)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        with open("Rectangle.json", "r") as file:
            json_str = file.read()
            json_data = json.loads(json_str)
            self.assertEqual(len(json_data), 2)
            self.assertEqual(json_data[0]['width'], r1.width)
            self.assertEqual(json_data[1]['height'], r2.height)

        with open("Square.json", "r") as file:
            json_str = file.read()
            json_data = json.loads(json_str)
            self.assertEqual(len(json_data), 2)
            self.assertEqual(json_data[0]['size'], s1.size)
            self.assertEqual(json_data[1]['size'], s2.size)

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string('[]'), [])
        self.assertEqual(
            Base.from_json_string(
                '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
            ),
            [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]
        )

    def test_load_from_file(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        s1 = Square(12, 3, 2, 1)
        s2 = Square(9, 4, 2, 1)

        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        rectangles = Rectangle.load_from_file()
        squares = Square.load_from_file()

        self.assertEqual(len(rectangles), 2)
        self.assertIsInstance(rectangles[0], Rectangle)
        self.assertIsInstance(rectangles[1], Rectangle)
        self.assertEqual(rectangles[0].width, r1.width)
        self.assertEqual(rectangles[1].height, r2.height)

        self.assertEqual(len(squares), 2)
        self.assertIsInstance(squares[0], Square)
        self.assertIsInstance(squares[1], Square)
        self.assertEqual(squares[0].size, s1.size)
        self.assertEqual(squares[1].size, s2.size)

    def test_save_to_file_csv(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(5, 4, 3, 2, 1)
        Rectangle.save_to_file_csv([r1, r2])

        with open("Rectangle.csv", "r") as file:
            csv_data = list(csv.reader(file))
            self.assertEqual(len(csv_data), 2)
            self.assertEqual(int(csv_data[0][1]), r1.width)
            self.assertEqual(int(csv_data[1][2]), r2.height)


if __name__ == "__main__":
    unittest.main()
