import unittest
from src.lab3.task2.age_groups import Survey


class TestSurvey(unittest.TestCase):
    def setUp(self):
        self.kino = Survey()

    def test_get_name_plus_age(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 30\nПетров Петр, 25\nСидоров Сидор, 40")
        self.kino.get_name_plus_age()
        expected_output = [[30, 'Иванов Иван'], [25, 'Петров Петр'], [40, 'Сидоров Сидор']]
        self.assertEqual(self.kino.name_plus_age, expected_output)

    def test_get_age_groups(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 30\nПетров Петр, 25\nСидоров Сидор, 40")
        self.kino.get_name_plus_age()
        self.kino.groups = [20, 30, 40]
        self.kino.get_age_groups()
        expected_age_groups = {'21-30': [('Иванов Иван', 30), ('Петров Петр', 25)], '31-40': [('Сидоров Сидор', 40)]}
        self.assertEqual(self.kino.age_groups, expected_age_groups)

    def test_printer(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 30\nПетров Петр, 25\nСидоров Сидор, 40")
        self.kino.get_name_plus_age()
        self.kino.groups = [20, 30, 40]
        self.kino.get_age_groups()
        result = self.kino.printer()
        expected_output = """21-30: Иванов Иван (30), Петров Петр (25) 
31-40: Сидоров Сидор (40) 
"""
        self.assertEqual(result, expected_output)

    def test_result(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 30\nПетров Петр, 25\nСидоров Сидор, 40")
        self.kino.groups = [20, 30, 40]
        result = self.kino.result()
        expected_output = """21-30: Иванов Иван (30), Петров Петр (25) 
31-40: Сидоров Сидор (40) 
"""
        self.assertEqual(result, expected_output)

    def test_result_empty_file(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("")
        self.kino.groups = [20, 30, 40]
        result = self.kino.result()
        expected_output = ''
        self.assertEqual(result, expected_output)

    def test_result_two_people_same_age(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 30\nПетров Петр, 30")
        self.kino.groups = [20, 30, 40]
        result = self.kino.result()
        expected_output = """21-30: Иванов Иван (30), Петров Петр (30) 
"""
        self.assertEqual(result, expected_output)

    def test_result_person_out_of_range(self):
        with open("input.txt", "w", encoding='UTF-8') as f:
            f.write("Иванов Иван, 50")
        self.kino.groups = [20, 30, 40]
        result = self.kino.result()
        expected_output = '40+: Иванов Иван (50) \n'
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()


