import unittest
from unittest.mock import MagicMock
from classes.movie_library import MovieLibrarySystem

class TestMovieLibrarySystemWithMock(unittest.TestCase):

    def setUp(self):
        """
        Setup with Mock objects.
        
        This method sets up the necessary mock objects for testing the MovieLibrarySystem.
        It mocks dependencies like `movie_class` and `user_class`, which are passed into the system under test (MovieLibrarySystem).
        The library object is instantiated with these mocks to simulate interactions with external classes.
        """  
        self.mock_movie = MagicMock()
        self.mock_user = MagicMock()
        self.library = MovieLibrarySystem(movie_class=self.mock_movie, user_class=self.mock_user)

    def test_add_movie(self):
        """
        Test add_movie with a mock.
        
        Data:
        - movie_data: a dictionary describing a movie.
        
        Steps:
        1. Call the `add_movie` method with the movie data.
        2. Verify that the `from_dict` method of the movie class was called with the provided data.
        3. Verify that the new movie was added to the `movies` list in MovieLibrarySystem.
        """
        movie_data = {"title": "Mock Movie", "director": "Mock Director", "release_year": 2022, "genre": "Drama", "rating": 7.5}
        self.library.add_movie(movie_data)
        self.mock_movie.from_dict.assert_called_once_with(movie_data)
        self.assertEqual(len(self.library.movies), 1)

    def test_register_user(self):
        """
        Test register_user with a mock.
        
        Data:
        - user_data: a dictionary containing user information.
        
        Steps:
        1. Call the `register_user` method with the user data.
        2. Verify that the `from_dict` method of the user class was called with the provided data.
        3. Verify that the new user was added to the `users` list in MovieLibrarySystem.
        """
        user_data = {"name": "Mock User", "email": "mock@example.com"}
        self.library.register_user(user_data)
        self.mock_user.from_dict.assert_called_once_with(user_data)
        self.assertEqual(len(self.library.users), 1)

    def test_track_viewing_status(self):
        """
        Test track_viewing_status with a mock.
        
        Data:
        - user_data: a dictionary with user data.
        - movie_data: a dictionary with movie data.
        - viewing_status: the viewing status.
        
        Steps:
        1. Register a user.
        2. Add a movie.
        3. Call the `track_viewing_status` method with the user's name, movie title, and status.
        4. Verify that the `set_viewing_status` method was called on the mock user object.
        """
        self.library.register_user({"name": "Mock User", "email": "mock@example.com"})
        self.library.add_movie({"title": "Mock Movie", "director": "Mock Director", "release_year": 2022, "genre": "Drama", "rating": 7.5})

        user_mock = self.mock_user.from_dict.return_value
        user_mock.get_user_name.return_value = "Mock User"
        self.library.track_viewing_status("Mock User", "Mock Movie", "watched")

        user_mock.set_viewing_status.assert_called_once_with("Mock Movie", "watched")

    def test_search_movies(self):
        """
        Test search_movies with a mock.
        
        Data:
        - criteria: a dictionary with search parameters.
        
        Steps:
        1. Add a mock movie to the `movies` list in MovieLibrarySystem.
        2. Call the `search_movies` method with search criteria.
        3. Verify that the `get_movie_title` method of the mock movie was called.
        4. Verify that the movie matching the criteria was found.
        """
        self.mock_movie.get_movie_title.return_value = "Mock Movie"
        self.library.movies = [self.mock_movie]

        criteria = {"title": "Mock Movie"}
        result = self.library.search_movies(criteria)

         # Verify that the method was called
        self.mock_movie.get_movie_title.assert_called_once()
        # Verify that one movie was found
        self.assertEqual(len(result), 1)
        # Verify that the found movie is the mock movie
        self.assertEqual(result[0], self.mock_movie)

if __name__ == '__main__':
    unittest.main()
