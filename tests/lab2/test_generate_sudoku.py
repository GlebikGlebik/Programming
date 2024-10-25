import unittest
from src.lab2.sudoku import *


class generate_sudokuTestCase(unittest.TestCase):

    def test_count_dots_one(self):
        grid = generate_sudoku(40)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 41)

    def test_count_dots_two(self):
        grid = generate_sudoku(0)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 81)

    def test_count_dots_three(self):
        grid = generate_sudoku(81)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 0)

    def test_puzzle1(self):
        grid = read_sudoku('puzzle1.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

    def test_puzzle2(self):
        grid = read_sudoku('puzzle2.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

    def test_puzzle3(self):
        grid = read_sudoku('puzzle3.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)