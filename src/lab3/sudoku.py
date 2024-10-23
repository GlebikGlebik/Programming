import pathlib
import typing as tp
import math

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> group([1,2], 1)
    Traceback (most recent call last):
        ...
    ValueError: Данный список невозможно поделить на подcписки с таким количеством элементов
    >>> group([2], 1)
    [[2]]
    >>> group([], 2)
    Traceback (most recent call last):
        ...
    ValueError: Список не может быть пустым
    >>> group([1, 2, 3], 5)
    Traceback (most recent call last):
        ...
    ValueError: Данный список невозможно поделить на подcписки с таким количеством элементов
    >>> group([1, 2, 3], 0)
    Traceback (most recent call last):
        ...
    ValueError: Размер группы не может быть нулевым или отрицательным
    """
    group_elements = []
    if n <= 0:
        raise ValueError("Размер группы не может быть нулевым или отрицательным")
    if len(values) == 0:
        raise ValueError("Список не может быть пустым")
    if len(values) // n != n:
        raise ValueError("Данный список невозможно поделить на подcписки с таким количеством элементов")
    for i in range(0, len(values), n):
        group_elements.append(values[i : i + n])
    return group_elements




def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos
    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    >>> get_row([['1', '2', '3', '4', '5'], ['6', '7', '8', '.', '.'], ['.', '.', '9', '.', '10']], (2, 0))
    ['.', '.', '9', '.', '10']
    >>> get_row([['.', '.', '9', '.', '1', '2', '3'], ['.', '.', '9', '.', '1', '2', '3'], ['4', '5', '6', '7', '8', '9', '10']], (1, 0))
    ['.', '.', '9', '.', '1', '2', '3']
    >>> get_row([['5']], (0, 0))
    ['5']
    """
    row, col = pos
    return grid[row]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos
    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    >>> get_col([['.', '.', '12', '34', '.', '56', '78', '90', '.'], ['.', '23', '.', '45', '67', '.', '.', '89', '10'], ['11', '.', '13', '14', '.', '15', '16', '.', '17'], ['.', '.', '18', '19', '20', '.', '21', '22', '23'], ['24', '.', '25', '26', '.', '.', '27', '28', '29'], ['30', '.', '31', '32', '33', '.', '34', '35', '36'], ['37', '38', '.', '39', '40', '41', '.', '42', '43'], ['.', '.', '44', '45', '46', '.', '47', '48', '49'], ['50', '.', '51', '52', '53', '.', '54', '55', '56']], (6,2))
    ['12', '.', '13', '18', '25', '31', '.', '44', '51']
    >>> get_col([['57', '58', '.', '59', '60', '.', '61', '62', '63'], ['64', '65', '66', '.', '67', '68', '.', '69', '70'], ['71', '72', '.', '73', '74', '75', '.', '76', '77'], ['78', '.', '79', '80', '.', '81', '.', '82', '83'], ['84', '85', '.', '86', '87', '88', '.', '89', '90'], ['91', '.', '92', '93', '94', '95', '.', '96', '97'], ['98', '99', '.', '100', '101', '.', '102', '103', '104'], ['105', '.', '106', '107', '.', '108', '109', '110', '111'], ['112', '113', '114', '.', '115', '116', '.', '117', '118'], ['119', '.', '120', '121', '122', '.', '123', '124', '125']], (4,7))
    ['62', '69', '76', '82', '89', '96', '103', '110', '117', '124']
    >>> get_col([['8']], (0,0))
    ['8']
    """
    row, col = pos
    col_elements = []
    for i in grid:
        col_elements.append(i[col])
    return col_elements


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos
    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    block_size = int(math.sqrt(len(grid)))
    start_row = (row // block_size) * block_size
    start_col = (col // block_size) * block_size
    block_elements = []
    for r in range(start_row, start_row + block_size):
        for c in range(start_col, start_col + block_size):
            block_elements.append(grid[r][c])
    return block_elements


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле
    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    >>> find_empty_positions([['5', '3', '.', '.', '7', '.', '.', '.', '.'], ['6', '.', '.', '1', '9', '5', '.', '.', '.'], ['.', '9', '8', '.', '.', '.', '.', '6', '.'], ['8', '.', '.', '.', '6', '.', '.', '.', '3'], ['4', '.', '.', '8', '.', '3', '.', '.', '1'], ['7', '.', '.', '.', '2', '.', '.', '.', '6'], ['.', '6', '.', '.', '.', '.', '2', '8', '.'], ['.', '.', '4', '1', '9', '5', '.', '.', '.'], ['.', '.', '.', '8', '.', '.', '.', '7', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['4', '5', '6', '7', '8', '9', '1', '2', '3'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '4', '5', '6', '7', '8', '9', '1'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '6', '7'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']])
    ()
    >>> find_empty_positions([['1', '2', '3', '4', '5', '6', '7', '8', '9'], ['4', '.', '6', '7', '8', '9', '1', '2', '3'], ['7', '8', '9', '1', '2', '3', '4', '5', '6'], ['2', '3', '.', '5', '6', '7', '8', '9', '1'], ['5', '6', '7', '8', '9', '1', '2', '3', '4'], ['8', '9', '1', '2', '3', '4', '5', '.', '7'], ['3', '4', '5', '6', '7', '8', '9', '1', '2'], ['6', '7', '8', '9', '1', '2', '3', '4', '5'], ['9', '1', '2', '3', '4', '5', '6', '7', '8']])
    (1, 1)
    """
    row = 0
    empty_pos = ()
    flag = True
    for i in grid:
        for col in range(len(i)):
            if i[col] == '.':
                empty_pos = (row, col)
                flag = False
                break
        if not flag:
            break
        row += 1
    return empty_pos

def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции
    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    >>> values = find_possible_values(grid, (8,4))
    >>> values == {'3', '5'}
    True
    >>> values = find_possible_values(grid, (8,8))
    >>> values == {'4'}
    True
    """
    not_pos_val = set()
    pos_val = set()
    [not_pos_val.add(i) for i in get_block(grid, pos)]
    [not_pos_val.add(i) for i in get_row(grid, pos)]
    [not_pos_val.add(i) for i in get_col(grid, pos)]
    for j in range(1,10):
        if str(j) not in not_pos_val:
            pos_val.add(str(j))
    return pos_val

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    #""" Решение пазла, заданного в grid """
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла
    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    empty_pos = find_empty_positions(grid)
    if empty_pos == ():
        return grid
    row, col = empty_pos
    pos_val = find_possible_values(grid, empty_pos)
    print(pos_val)
    if pos_val != set():
        for i in pos_val:
            grid[row][col] = i
        print(display(grid), "\n")
        return solve(grid)
    empty_pos = find_empty_positions(grid)
    row, col = empty_pos
    pos_val = find_possible_values(grid, empty_pos)
    print(pos_val)
    for i in pos_val:
        grid[row][col] = i
    print(display(grid), "\n")
    return grid
    # *_*

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    # TODO: Add doctests with bad puzzles
    pass


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    pass


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)