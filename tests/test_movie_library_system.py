import unittest
from unittest.mock import MagicMock
from classes.movie_library import MovieLibrarySystem

class TestMovieLibrarySystemWithMock(unittest.TestCase):

    def setUp(self):
        """Setup with Mock objects."""
        self.mock_movie = MagicMock()
        self.mock_user = MagicMock()
        self.library = MovieLibrarySystem(movie_class=self.mock_movie, user_class=self.mock_user)

    def test_add_movie(self):
        """Test add_movie with a mock."""
        movie_data = {"title": "Mock Movie", "director": "Mock Director", "release_year": 2022, "genre": "Drama", "rating": 7.5}
        self.library.add_movie(movie_data)
        self.mock_movie.from_dict.assert_called_once_with(movie_data)
        self.assertEqual(len(self.library.movies), 1)

    def test_register_user(self):
        """Test register_user with a mock."""
        user_data = {"name": "Mock User", "email": "mock@example.com"}
        self.library.register_user(user_data)
        self.mock_user.from_dict.assert_called_once_with(user_data)
        self.assertEqual(len(self.library.users), 1)

    def test_track_viewing_status(self):
        """Test track_viewing_status with a mock."""
        self.library.register_user({"name": "Mock User", "email": "mock@example.com"})
        self.library.add_movie({"title": "Mock Movie", "director": "Mock Director", "release_year": 2022, "genre": "Drama", "rating": 7.5})

        user_mock = self.mock_user.from_dict.return_value
        user_mock.get_user_name.return_value = "Mock User"
        self.library.track_viewing_status("Mock User", "Mock Movie", "watched")

        user_mock.set_viewing_status.assert_called_once_with("Mock Movie", "watched")

    def test_search_movies(self):
        """Test search_movies with a mock."""
        self.mock_movie.get_movie_title.return_value = "Mock Movie"
        self.library.movies = [self.mock_movie]

        criteria = {"title": "Mock Movie"}
        result = self.library.search_movies(criteria)

        self.mock_movie.get_movie_title.assert_called_once()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], self.mock_movie)

if __name__ == '__main__':
    unittest.main()
