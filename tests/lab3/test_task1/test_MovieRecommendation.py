import unittest
import tempfile
import os
from src.lab3.task1.MovieRecommendation import *

class MovieRecommendationTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем временные файлы для фильмов и пользователей
        self.films_data = "1,Дюна\n2,Мстители: Финал\n3,Хатико\n4,Унесенные призраками\n"
        self.users_data = "1,2,3\n2,3,4\n3,4,5\n4,5,6\n"

        self.films_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
        self.users_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')

        self.films_file.write(self.films_data)
        self.films_file.close()

        self.users_file.write(self.users_data)
        self.users_file.close()

        # Инициализируем экземпляр класса
        self.movie_recommendation = MovieRecommendation()
        self.movie_recommendation.films_file = self.films_file.name
        self.movie_recommendation.users_file = self.users_file.name

    def tearDown(self):
        # Удаляем временные файлы после тестов
        os.remove(self.films_file.name)
        os.remove(self.users_file.name)

    def test_one(self):
        """Тестирует случай, когда совпадает ровно половина фильмов."""
        self.movie_recommendation.main_user_history = ['1', '2']
        self.movie_recommendation.result()
        self.assertEqual(self.movie_recommendation.film_name, "Дюна")

    def test_two(self):
        self.movie_recommendation.main_user_history = ['2', '3']
        self.movie_recommendation.result()
        self.assertEqual(self.movie_recommendation.film_name, "Мстители: Финал")

    def test_three(self):
        self.movie_recommendation.main_user_history = ['2', '4']
        self.movie_recommendation.result()
        self.assertEqual(self.movie_recommendation.film_name, "Дюна")

    def test_no_recommendation(self):
        """Тестирует случай, когда нет рекомендаций так как пользователь уже посмотрел все фильмы."""
        self.movie_recommendation.main_user_history = ['1', '2', '3', '4']
        self.movie_recommendation.result()
        self.assertEqual(self.movie_recommendation.film_name, "Подходящих рекомендаций для пользователя нет")

if __name__ == '__main__':
    unittest.main()