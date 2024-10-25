import unittest
from src.lab2.sudoku import *

class sudokuTestCase(unittest.TestCase):

    def test_solve_puzzle_one(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(solve(grid),
                         [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                          ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                          ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                          ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                          ['3', '4', '5', '2', '8', '6', '1', '7', '9']])

    def test_solve_puzzle_two(self):
        grid = read_sudoku('puzzle2.txt')
        self.assertEqual(solve(grid),
                         [['7', '9', '4', '5', '8', '2', '1', '3', '6'], ['2', '6', '8', '9', '3', '1', '7', '4', '5'],
                          ['3', '1', '5', '4', '7', '6', '9', '8', '2'], ['6', '8', '9', '7', '1', '5', '3', '2', '4'],
                          ['4', '3', '2', '8', '6', '9', '5', '7', '1'], ['1', '5', '7', '2', '4', '3', '8', '6', '9'],
                          ['8', '2', '1', '6', '5', '7', '4', '9', '3'], ['9', '4', '3', '1', '2', '8', '6', '5', '7'],
                          ['5', '7', '6', '3', '9', '4', '2', '1', '8']])

    def test_solve_puzzle_three(self):
        grid = read_sudoku('puzzle3.txt')
        self.assertEqual(solve(grid),
                         [['8', '3', '5', '4', '1', '6', '9', '2', '7'], ['2', '9', '6', '8', '5', '7', '4', '3', '1'],
                          ['4', '1', '7', '2', '9', '3', '6', '5', '8'], ['5', '6', '9', '1', '3', '4', '7', '8', '2'],
                          ['1', '2', '3', '6', '7', '8', '5', '4', '9'], ['7', '4', '8', '5', '2', '9', '1', '6', '3'],
                          ['6', '5', '2', '7', '8', '1', '3', '9', '4'], ['9', '8', '1', '3', '4', '5', '2', '7', '6'],
                          ['3', '7', '4', '9', '6', '2', '8', '1', '5']])

    def test_group_four_elements(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_group_nine_elements(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_group_sixteen_elements(self):
        self.assertEqual(group([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7], 4),
                         [[1, 2, 3, 4], [5, 6, 7, 8], [9, 1, 2, 3], [4, 5, 6, 7]])

    def test_group_one_element(self):
        self.assertEqual(group([1], 1), [[1]])

    def test_group_unresolved_n(self):
        with self.assertRaises(ValueError) as e:
            group([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7], 0)
        self.assertEqual('Размер группы не может быть нулевым или отрицательным', e.exception.args[0])

    def test_group_unresolved_array(self):
        with self.assertRaises(ValueError) as e:
            group([1, 2], 1)
        self.assertEqual('Данный список невозможно поделить на подcписки с таким количеством элементов',
                         e.exception.args[0])

    def test_group_zero_array(self):
        with self.assertRaises(ValueError) as e:
            group([], 1)
        self.assertEqual('Список не может быть пустым', e.exception.args[0])

    def test_get_row_one(self):
        self.assertEqual(get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '2', '.'])

    def test_get_row_two(self):
        self.assertEqual(
            get_row([['1', '2', '3', '4', '5'], ['6', '7', '8', '.', '.'], ['.', '.', '9', '.', '10']], (2, 0)),
            ['.', '.', '9', '.', '10'])

    def test_get_row_three(self):
        self.assertEqual(get_row([['.', '.', '9', '.', '1', '2', '3'], ['.', '.', '9', '.', '1', '2', '3'],
                                  ['4', '5', '6', '7', '8', '9', '10']], (1, 0)), ['.', '.', '9', '.', '1', '2', '3'])

    def test_get_col_one(self):
        self.assertEqual(get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0)), ['1', '4', '7'])

    def test_get_col_two(self):
        self.assertEqual(get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2)), ['3', '6', '9'])

    def test_get_col_three(self):
        self.assertEqual(get_col(
            [['.', '.', '12', '34', '.', '56', '78', '90', '.'], ['.', '23', '.', '45', '67', '.', '.', '89', '10'],
             ['11', '.', '13', '14', '.', '15', '16', '.', '17'], ['.', '.', '18', '19', '20', '.', '21', '22', '23'],
             ['24', '.', '25', '26', '.', '.', '27', '28', '29'], ['30', '.', '31', '32', '33', '.', '34', '35', '36'],
             ['37', '38', '.', '39', '40', '41', '.', '42', '43'], ['.', '.', '44', '45', '46', '.', '47', '48', '49'],
             ['50', '.', '51', '52', '53', '.', '54', '55', '56']], (6, 2)),
                         ['12', '.', '13', '18', '25', '31', '.', '44', '51'])

    def test_get_col_four(self):
        self.assertEqual(get_col(
            [['57', '58', '.', '59', '60', '.', '61', '62', '63'], ['64', '65', '66', '.', '67', '68', '.', '69', '70'],
             ['71', '72', '.', '73', '74', '75', '.', '76', '77'], ['78', '.', '79', '80', '.', '81', '.', '82', '83'],
             ['84', '85', '.', '86', '87', '88', '.', '89', '90'], ['91', '.', '92', '93', '94', '95', '.', '96', '97'],
             ['98', '99', '.', '100', '101', '.', '102', '103', '104'],
             ['105', '.', '106', '107', '.', '108', '109', '110', '111'],
             ['112', '113', '114', '.', '115', '116', '.', '117', '118'],
             ['119', '.', '120', '121', '122', '.', '123', '124', '125']], (4, 7)),
                         ['62', '69', '76', '82', '89', '96', '103', '110', '117', '124'])

    def test_get_col_five(self):
        self.assertEqual(get_col([['8']], (0, 0)), ['8'])

    def test_get_block_one(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(get_block(grid, (0, 1)), ['5', '3', '.', '6', '.', '.', '.', '9', '8'])

    def test_get_block_two(self):
        grid = read_sudoku('puzzle2.txt')
        self.assertEqual(get_block(grid, (4, 7)), ['.', '.', '.', '.', '.', '.', '.', '6', '.'])

    def test_get_block_three(self):
        grid = read_sudoku('puzzle3.txt')
        self.assertEqual(get_block(grid, (8, 8)), ['.', '9', '.', '.', '.', '.', '.', '.', '5'])

    def test_count_dots_one(self):
        grid = generate_sudoku(40)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 41)

    def test_count_dots_two(self):
        grid = generate_sudoku(0)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 81)

    def test_count_dots_three(self):
        grid = generate_sudoku(81)
        self.assertEqual(sum(1 for row in grid for e in row if e == '.'), 0)

    def test_solve_puzzle1_check_solution(self):
        grid = read_sudoku('puzzle1.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

    def test_solve_puzzle2_check_solution(self):
        grid = read_sudoku('puzzle2.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

    def test_solve_puzzle3_check_solution(self):
        grid = read_sudoku('puzzle3.txt')
        solution = solve(grid)
        self.assertEqual(check_solution(solution), True)

    def test_find_empty_positions_one(self):
        self.assertEqual(find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']]), (0, 2))

    def test_find_empty_positions_two(self):
        self.assertEqual(find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']]), (1, 1))

    def test_find_empty_positions_three(self):
        self.assertEqual(find_empty_positions(
            [['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '4', '1', '9', '5', '.', '.', '.'],
             ['.', '.', '.', '8', '.', '.', '.', '7', '9']]), (0, 2))

    def test_find_empty_positions_four(self):
        self.assertEqual(find_empty_positions(
            [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'],
             ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'],
             ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'],
             ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
             ['9', '1', '2', '3', '4', '5', '6', '7', '8']]), ())

    def test_find_empty_positions_five(self):
        self.assertEqual(find_empty_positions(
            [['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['4', '.', '6', '7', '8', '9', '1', '2', '3'],
             ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '.', '5', '6', '7', '8', '9', '1'],
             ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '.', '7'],
             ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'],
             ['9', '1', '2', '3', '4', '5', '6', '7', '8']]), (1, 1))

    def test_find_possible_values_one(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (0, 2)), {'1', '2', '4'})

    def test_find_possible_values_two(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (4, 7)), {'2', '5', '9'})

    def test_find_possible_values_three(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (8, 4)), {'3', '5'})

    def test_find_possible_values_five(self):
        grid = read_sudoku('puzzle1.txt')
        self.assertEqual(find_possible_values(grid, (8, 8)), {'4'})