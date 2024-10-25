import unittest
from src.lab3.sudoku import *


class check_solutionTestCase(unittest.TestCase):

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