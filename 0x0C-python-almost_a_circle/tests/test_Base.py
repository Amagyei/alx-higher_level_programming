#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_init_with_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj_with_id = Base(id = 10)
        self.assertEqual(obj_with_id.id, 10)

    def test_init_without_id(self):
        obj_1 = Base()
        obj_2 = Base()
        self.assertNotEqual(obj_1.id, obj_2.id)

    def test_nb_objects_increment(self):
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(obj_2.id, obj_1.id + 1)


if __name__ == '__main__':
    unittest.main()