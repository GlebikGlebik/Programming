import unittest
from src.lab2.sudoku import *


class Get_blockTestCase(unittest.TestCase):

    def test_one(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])

    def test_two(self):
        grid = read_sudoku('puzzle2.txt')
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '.', '.', '.', '.', '.', '6', '.'])

    def test_three(self):
        grid = read_sudoku('puzzle3.txt')
        self.assertEqual(get_block(grid, (8, 8)), ['.', '9', '.', '.', '.', '.', '.', '.', '5'])

