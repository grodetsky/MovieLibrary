import unittest
from classes.movie import Movie
from classes.user import User
from classes.movie_library import MovieLibrarySystem


class TestMovieLibrarySystem(unittest.TestCase):

    def setUp(self):
        # Create instances of Movie and User classes
        self.movie1 = Movie("Test Movie", "John Doe", 2024, "Action", 8.5)
        self.movie2 = Movie("Another Movie", "Jane Doe", 2023, "Comedy", 7.2)
        self.user1 = User("Test User", "test@example.com")
        self.user2 = User("Another User", "another@example.com")

        # Create an instance of the MovieLibrarySystem
        self.library = MovieLibrarySystem(movie_class=Movie, user_class=User)

    def test_add_movie(self):
        """Test adding a movie to the library."""
        self.library.add_movie({"title": "Test Movie", "director": "John Doe", "release_year": 2024, "genre": "Action", "rating": 8.5})
        self.assertEqual(len(self.library.movies), 1)
        self.assertEqual(self.library.movies[0].get_movie_title(), "Test Movie")

    def test_remove_movie(self):
        """Test removing a movie from the library."""
        self.library.add_movie({"title": "Test Movie", "director": "John Doe", "release_year": 2024, "genre": "Action", "rating": 8.5})
        self.library.add_movie({"title": "Another Movie", "director": "Jane Doe", "release_year": 2023, "genre": "Comedy", "rating": 7.2})

        self.library.remove_movie("Test Movie")  # Use the movie title to remove it
        self.assertEqual(len(self.library.movies), 1)
        self.assertEqual(self.library.movies[0].get_movie_title(), "Another Movie")

    def test_register_user(self):
        """Test registering a user in the system."""
        self.library.register_user({"name": "Test User", "email": "test@example.com"})
        self.assertEqual(len(self.library.users), 1)
        self.assertEqual(self.library.users[0].get_user_name(), "Test User")

    def test_track_viewing_status(self):
        """Test tracking the viewing status for a user."""
        self.library.register_user({"name": "Test User", "email": "test@example.com"})
        self.library.add_movie(
            {"title": "Test Movie", "director": "John Doe", "release_year": 2024, "genre": "Action", "rating": 8.5})

        # Add the movie to the user's collection
        user = self.library.users[0]
        movie = self.library.movies[0]
        user.add_movie(movie)

        # Assign a viewing status
        self.library.track_viewing_status("Test User", "Test Movie", "watched")

        # Verify that the status was updated
        self.assertEqual(user.get_viewing_status("Test Movie"), "watched")

    def test_search_movies(self):
        """Test searching for movies based on different criteria."""
        self.library.add_movie({"title": "Test Movie", "director": "John Doe", "release_year": 2024, "genre": "Action", "rating": 8.5})
        self.library.add_movie({"title": "Another Movie", "director": "Jane Doe", "release_year": 2023, "genre": "Comedy", "rating": 7.2})

        criteria = {"title": "Test Movie"}
        result = self.library.search_movies(criteria)

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_movie_title(), "Test Movie")


if __name__ == '__main__':
    unittest.main()
