import unittest
import tempfile
import os
from src.lab3.task1.MovieRecommendation import MovieRecommendation

class MovieRecommendationTestCase(unittest.TestCase):
    def setUp(self):
        # Инициализируем экземпляр класса
        self.movie_recommendation = MovieRecommendation()

    def test_one(self):
        """Тестирует случай, когда совпадает ровно половина фильмов."""
        self.movie_recommendation.main_user_history = ['1', '2']
        result = self.movie_recommendation.result()
        self.assertEqual(result, "Дюна")

    def test_two(self):
        """Тестирует случай, когда совпадает половина фильмов с другим набором."""
        self.movie_recommendation.main_user_history = ['2', '3']
        result = self.movie_recommendation.result()
        self.assertEqual(result, "Мстители: Финал")

    def test_three(self):
        """Тестирует случай, когда совпадает половина фильмов с другим набором."""
        self.movie_recommendation.main_user_history = ['2', '4']
        result = self.movie_recommendation.result()
        self.assertEqual(result, "Дюна")

    def test_no_recommendation(self):
        """Тестирует случай, когда нет рекомендаций так как пользователь уже посмотрел все фильмы."""
        self.movie_recommendation.main_user_history = ['1', '2', '3', '4']
        result = self.movie_recommendation.result()
        self.assertEqual(result, "Подходящих рекомендаций для пользователя нет")

    def test_empty_main_user_movies(self):
        """Тестирует случай, когда пользователь не смотрел ни одного фильма."""
        self.movie_recommendation.main_user_history = []
        result = self.movie_recommendation.result()
        self.assertIn(result, ['Мстители: Финал', 'Хатико', 'Дюна', 'Унесенные призраками'])

if __name__ == '__main__':
    unittest.main()
