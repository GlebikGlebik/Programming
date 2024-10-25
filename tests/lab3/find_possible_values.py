import unittest
from src.lab3.sudoku import *


class find_possible_valuesTestCase(unittest.TestCase):

    def test_one(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (0,2)), {'1', '2', '4'})

    def test_two(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (4,7)), {'2', '5', '9'})

    def test_three(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (8,4)), {'3', '5'})

    def test_five(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (8,8)), {'4'})