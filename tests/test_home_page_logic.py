import unittest
import os
from classes.user import User
from classes.movie import Movie
from GUI_logic.home_page import show_account_info, show_movies_info

class TestHomePageLogic(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.test_users_file = "users.json"
        self.test_movies_file = "movies.json"

        # Mock users
        self.mock_users = [
            User(name="test_user", email="test@example.com"),
            User(name="another_user", email="another@example.com"),
        ]
        User.save_to_json(self.mock_users, self.test_users_file)

        # Mock movies
        self.mock_movies = [
            Movie(title="Inception", director="Christopher Nolan", release_year=2010, genre="Sci-Fi", rating=8.8),
            Movie(title="The Matrix", director="The Wachowskis", release_year=1999, genre="Action", rating=8.7),
        ]
        Movie.save_to_json(self.mock_movies, self.test_movies_file)

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_users_file):
            os.remove(self.test_users_file)
        if os.path.exists(self.test_movies_file):
            os.remove(self.test_movies_file)

    def test_show_account_info_user_exists(self):
        """Test account info retrieval for existing user."""
        user_data = show_account_info("test_user")
        self.assertIsNotNone(user_data)
        self.assertEqual(user_data["name"], "test_user")
        self.assertIn("email", user_data)

    def test_show_account_info_user_not_found(self):
        """Test account info retrieval for non-existing user."""
        user_data = show_account_info("non_existing_user")
        self.assertIsNone(user_data)

    def test_show_movies_info_movies_exist(self):
        """Test movies info retrieval when movies exist."""
        movies = show_movies_info()
        self.assertEqual(len(movies), 2)
        self.assertEqual(movies[0].get_movie_title(), "Inception")

    def test_show_movies_info_no_movies(self):
        """Test movies info retrieval when no movies exist."""
        os.remove(self.test_movies_file)
        movies = show_movies_info()
        self.assertEqual(len(movies), 0)

if __name__ == "__main__":
    unittest.main()
