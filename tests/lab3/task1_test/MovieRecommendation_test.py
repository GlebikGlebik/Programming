import unittest
from src.lab3.task1.MovieRecommendation import *

class MovieRecommendationTestCase(unittest.TestCase):
    def test_one(self):
        """Тестирует случай, когда совпадает ровно половина фильмов."""
        main_user_history = ['1','2']
        self.assertEqual(MovieRecommendation.main(main_user_history), "Дюна")

    def test_two(self):
        main_user_history = ['2', '3']
        self.assertEqual(MovieRecommendation.main(main_user_history), "Мстители: Финал")

    def test_three(self):
        main_user_history = ['2', '4']
        self.assertEqual(MovieRecommendation.main(main_user_history), "Дюна")

    def test_no_recommendation(self):
        """Тестирует случай, когда нет рекомендаций так как пользователь уже посмотрел все фильмы"""
        main_user_history = [1, 2, 3, 4]
        self.assertEqual(MovieRecommendation.main(main_user_history), "Подходящих рекомендаций для пользователя нет")

    def test_empty_main_user_movies(self):
        """Тестирует случай, когда пользователь не смотрел ни одного фильма."""
        main_user_history = list()
        self.assertIn(MovieRecommendation.main(main_user_history), ['Мстители: Финал', 'Хатико', 'Дюна', 'Унесенные призраками'])


if __name__ == '__main__':
    unittest.main()