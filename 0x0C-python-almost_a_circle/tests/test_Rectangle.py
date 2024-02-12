#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class testRectangle(unittest.TestCase):
    
    """
    Tests for width
    """

    def test_width_not_int(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(width=-1.2)
            self.assertNotEqual(obj.width, -1.2)
    
    def test_width_less_than_zer0(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(width=-1, height=1)
            self.assertNotEqual(obj.width, -1)
    
    def test_width_zer0(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(width=0, height=1)
            self.assertNotEqual(obj.width, 0)

    def test_width_pos_int(self):
        obj = Rectangle(width = 2, height=2)
        self.assertEqual(obj.width, 2)

    """
    Tests for height
    """

    def test_height_not_int(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(height=-1.2)
            self.assertNotEqual(obj.height, -1.2)

    def test_height_as_string(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(width=1, height = "a", x = 1, y = 1)
            self.assertNotEqual(obj.height, "a")

    def test_height_less_than_zer0(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(height=-1, width=1 )
            self.assertNotEqual(obj.height, -1)

    def test_height_zer0(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(width=-1, height=1)
            self.assertNotEqual(obj.width, -1)

    def test_height_pos_int(self):
        obj = Rectangle(width = 2, height=2)
        self.assertEqual(obj.height, 2)

    """
    Tests for x
    """

    def test_x_not_int(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(x=-1.2)
            self.assertNotEqual(obj.x, -1.2)

    def test_x_as_string(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(width=1, height = 1, x = "a", y=1)
            self.assertNotEqual(obj.x, "a")

    def test_x_less_than_zer0(self):
        with self.assertRaises(ValueError):
            obj = Rectangle(x=-1, width=1, height=1)
            self.assertNotEqual(obj.x, -1)
    
    def test_x_zero(self):
        obj = Rectangle(width=1, height=1, x=0 )
        self.assertEqual(obj.x, 0)

    def test_width_pos_int(self):
        obj = Rectangle(width = 2, height=2, x = 2)
        self.assertEqual(obj.x, 2)

    """
    Tests for y
    """

    def test_y_not_int(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(y=-1.2)
            self.assertNotEqual(obj.y, -1.2)

    def test_y_as_string(self):
        with self.assertRaises(TypeError):
            obj = Rectangle(width=1, height = 1, x = 1, y="a")
            self.assertNotEqual(obj.y, "a")

    def test_y_greater_than_zer0(self):
        obj = Rectangle(y=1, width=1, height=1)
        self.assertEqual(obj.y, 1)

    def test_y_zero(self):
        obj = Rectangle(width=1, height=1, y=0)
        self.assertEqual(obj.y, 0)

    def test_width_pos_int(self):
        obj = Rectangle(width = 2, height=2, y = 2)
        self.assertEqual(obj.y, 2)


    

