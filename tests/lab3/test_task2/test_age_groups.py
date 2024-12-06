import unittest
import os
from src.lab3.task2.age_groups import *

class TestSurvey(unittest.TestCase):

    def setUp(self):
        # Создаем файл input.txt с тестовыми данными перед каждым тестом
        self.test_file = 'input.txt'
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('Alice,25\nBob,30\nCharlie,15\n')

    def tearDown(self):
        # Удаляем файл после завершения тестов
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_get_name_plus_age(self):
        expected_output = [[25, 'Alice'], [30, 'Bob'], [15, 'Charlie']]
        result = Survey.get_name_plus_age()
        self.assertEqual(result, expected_output)

    def test_get_age_groups(self):
        name_plus_age = [(25, 'Alice'), (30, 'Bob'), (15, 'Charlie')]
        expected_output = {
            '0-18': [('Charlie', 15)],
            '19-25': [('Alice', 25)],
            '26-35': [('Bob', 30)],
            '36-45': [],
            '46-60': [],
            '61-80': [],
            '81-100': [],
            '101+': []
        }
        result = Survey.get_age_groups(name_plus_age)
        self.assertEqual(result, expected_output)

    def test_printer(self):
        age_groups = {
            '0-18': [('Charlie', 15)],
            '19-25': [('Alice', 25)],
            '26-35': [('Bob', 30)],
            '36-45': [],
            '46-60': [],
            '61-80': [],
            '81-100': [],
            '101+': []
        }
        expected_output = '0-18: Charlie (15) \n19-25: Alice (25) \n26-35: Bob (30) \n'
        result = Survey.printer(age_groups)
        self.assertEqual(result, expected_output)

    def test_same_age(self):
        # Тестируем случай, когда все участники имеют одинаковый возраст
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('Alice,30\nBob,30\nCharlie,30\n')
        name_plus_age = [(30, 'Alice'), (30, 'Bob'), (30, 'Charlie')]
        expected_output = {
            '0-18': [],
            '19-25': [],
            '26-35': [('Alice', 30), ('Bob', 30), ('Charlie', 30)],
            '36-45': [],
            '46-60': [],
            '61-80': [],
            '81-100': [],
            '101+': []
        }
        result = Survey.get_age_groups(name_plus_age)
        self.assertEqual(result, expected_output)

    def test_age_groups_with_multiple_ages(self):
        # Тестируем поведение с участниками в разных возрастных группах
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('Alice,25\nBob,30\nCharlie,15\nDavid,40\nEve,70\nFrank,90\n')
        name_plus_age = [(25, 'Alice'), (30, 'Bob'), (15, 'Charlie'), (40, 'David'), (70, 'Eve'), (90, 'Frank')]
        expected_output = {
            '0-18': [('Charlie', 15)],
            '19-25': [('Alice', 25)],
            '26-35': [('Bob', 30)],
            '36-45': [('David', 40)],
            '46-60': [],
            '61-80': [('Eve', 70)],
            '81-100': [('Frank', 90)],
            '101+': []
        }
        result = Survey.get_age_groups(name_plus_age)
        self.assertEqual(result, expected_output)

    def test_empty_file(self):
        # Тестируем поведение с пустым файлом
        with open(self.test_file, 'w', encoding='utf-8') as f:
            f.write('')
        expected_output = []
        result = Survey.get_name_plus_age()
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()