import unittest
from src.lab4.big_cool_task import *

class TestBigCoolTask(unittest.TestCase):
    def setUp(self):
        self.ord = Orders()

    def test_exact_match(self):
        # given
        self.ord.orders = [{'ID': 31987, 'Products': ['Сыр', ' Колбаса', ' Сыр', ' Макароны', ' Колбаса'], 'FIO': 'Петрова Анна', 'Address': 'Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки', 'Number': '+7-921-456-78-90', 'Priority': 'MIDDLE'}, {'ID': 87459, 'Products': ['Молоко', ' Яблоки', ' Хлеб', ' Яблоки', ' Молоко'], 'FIO': 'Иванов Иван Иванович', 'Address': 'Россия. Московская область. Москва. улица Пушкина', 'Number': '+7-912-345-67-89', 'Priority': 'MAX'}, {'ID': 31987, 'Products': ['Сыр', ' Колбаса', ' Макароны', ' Сыр', ' Колбаса'], 'FIO': 'Петрова Анна Сергеевна', 'Address': 'Франция. Иль-де-Франс. Париж. Шанз-Элизе', 'Number': '+3-214-020-50-50', 'Priority': 'MIDDLE'}, {'ID': 56342, 'Products': ['Хлеб', ' Молоко', ' Хлеб', ' Молоко'], 'FIO': 'Смирнова Мария Леонидовна', 'Address': 'Германия. Бавария. Мюнхен. Мариенплац', 'Number': '+4-989-234-56', 'Priority': 'LOW'}, {'ID': 48276, 'Products': ['Яблоки', ' Макароны', ' Яблоки'], 'FIO': 'Алексеев Алексей Алексеевич', 'Address': 'Италия. Лацио. Рим. Колизей', 'Number': '+3-061-234-56-78', 'Priority': 'MAX'}, {'ID': 65829, 'Products': ['Сок', ' Вода', ' Сок', ' Вода'], 'FIO': 'Белова Екатерина Михайловна', 'Address': 'Испания. Каталония. Барселона. Рамбла', 'Number': '+34-93-1234-567', 'Priority': 'LOW'}, {'ID': 72901, 'Products': ['Чай', ' Кофе', ' Чай', ' Кофе'], 'FIO': 'Михайлов Сергей Петрович', 'Address': 'Великобритания. Англия. Лондон. Бейкер-стрит', 'Number': '+4-207-946-09-58', 'Priority': 'LOW'}, {'ID': 84756, 'Products': ['Печенье', ' Сыр', ' Печенье', ' Сыр'], 'FIO': 'Васильева Анна Владимировна', 'Address': 'Япония. Шибуя. Шибуя-кроссинг', 'Number': '+8-131-234-5678', 'Priority': 'MAX'}, {'ID': 90385, 'Products': ['Макароны', ' Сыр', ' Макароны', ' Сыр'], 'FIO': 'Николаев Николай', 'Address': '', 'Number': '+1-416-123-45-67', 'Priority': 'LOW'}]
        expected_result = ['87459;Молоко x2, Яблоки x2, Хлеб;Иванов Иван Иванович;Россия. Московская область. Москва. улица Пушкина;+7-912-345-67-89;MAX\n', '31987;Сыр x2, Колбаса x2, Макароны;Петрова Анна;Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки;+7-921-456-78-90;MIDDLE\n', '72901;Чай x2, Кофе x2;Михайлов Сергей Петрович;Великобритания. Англия. Лондон. Бейкер-стрит;+4-207-946-09-58;LOW\n', '48276;Яблоки x2, Макароны;Алексеев Алексей Алексеевич;Италия. Лацио. Рим. Колизей;+3-061-234-56-78;MAX\n', '31987;Сыр x2, Колбаса x2, Макароны;Петрова Анна Сергеевна;Франция. Иль-де-Франс. Париж. Шанз-Элизе;+3-214-020-50-50;MIDDLE\n']

        # when
        self.ord.result_function()
        result = self.ord.valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)

    def test_empty_address(self):
        # given
        self.ord.orders = [{'ID': 12345, 'Products': ['Хлеб'], 'FIO': 'Иванов Иван', 'Address': '', 'Number': '+7-911-111-11-11', 'Priority': 'LOW'}]
        expected_result = []

        # when
        self.ord.result_function()
        result = self.ord.valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)

    def test_empty_address_2(self):
        # given
        self.ord.orders = [{'ID': 12345, 'Products': ['Хлеб'], 'FIO': 'Иванов Иван', 'Address': '', 'Number': '+7-911-111-11-11', 'Priority': 'LOW'}]
        expected_result = ['12345;1;no data\n']

        # when
        self.ord.result_function()
        result = self.ord.non_valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)


    def test_non_valid_input_1(self):
        # given
        self.ord.orders = [{'ID': 12349, 'Products': ['Вино'], 'FIO': 'Кузнецов Кузьма', 'Address': 'Франция. Париж. Елисейские поля', 'Number': '+3-121-235-67-67', 'Priority': 'LOW'}]
        expected_result = ['12349;1;Франция. Париж. Елисейские поля\n']

        # when
        self.ord.result_function()
        result = self.ord.non_valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)

    def test_non_valid_input_2(self):
        # given
        self.ord.orders = [{'ID': 12349, 'Products': ['Вино'], 'FIO': 'Кузнецов Кузьма', 'Address': 'Франция. Париж. Елисейские поля', 'Number': '+33-1-2345-6789', 'Priority': 'LOW'}]
        expected_result = ['12349;2;+33-1-2345-6789\n', '12349;1;Франция. Париж. Елисейские поля\n']

        # when
        self.ord.result_function()
        result = self.ord.non_valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)

    def test_non_valid_input_3(self):
        # given
        self.ord.orders = [{'ID': 12349, 'Products': ['Вино'], 'FIO': 'Кузнецов Кузьма', 'Address': 'Франция. Париж. Елисейские поля. Кутузовка', 'Number': '+33-1-2345-6789', 'Priority': 'LOW'}]
        expected_result = ['12349;2;+33-1-2345-6789\n']

        # when
        self.ord.result_function()
        result = self.ord.non_valid_arr_for_tests

        # then
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()