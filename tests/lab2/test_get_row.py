import unittest
from src.lab2.sudoku import *


class Get_rowTestCase(unittest.TestCase):

    def test_one(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])

    def test_two(self):
        self.assertEqual(
            get_row([['1', '2', '3', '4', '5'], ['6', '7', '8', '.', '.'], ['.', '.', '9', '.', '10']], (2, 0)),
            ['.', '.', '9', '.', '10'])

    def test_three(self):
        self.assertEqual(get_row([['.', '.', '9', '.', '1', '2', '3'], ['.', '.', '9', '.', '1', '2', '3'],
                                  ['4', '5', '6', '7', '8', '9', '10']], (1, 0)), ['.', '.', '9', '.', '1', '2', '3'])
