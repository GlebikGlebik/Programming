import unittest
from src.lab2.sudoku import *


class GroupTestCase(unittest.TestCase):

    def test_four_elements(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_nine_elements(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_sixteen_elements(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7], 4),
                         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])

    def test_one_element(self):
        self.assertEqual(group([1], 1), [[1]])

    def test_unresolved_n(self):
        with self.assertRaises(ValueError) as e:
            group([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7], 0)
        self.assertEqual('Размер группы не может быть нулевым или отрицательным', e.exception.args[0])

    def test_unresolved_array(self):
        with self.assertRaises(ValueError) as e:
            group([1,2], 1)
        self.assertEqual('Данный список невозможно поделить на подcписки с таким количеством элементов', e.exception.args[0])

    def test_zero_array(self):
        with self.assertRaises(ValueError) as e:
            group([], 1)
        self.assertEqual('Список не может быть пустым', e.exception.args[0])