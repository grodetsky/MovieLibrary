import unittest
from classes.movie_library import MovieLibrarySystem
from classes.movie import Movie
from classes.user import User

class TestMovieLibrarySystem(unittest.TestCase):

    def setUp(self):
        """Initialization before each test"""
        self.library = MovieLibrarySystem()
        self.movie_data = {
            "title": "Inception",
            "director": "Christopher Nolan",
            "release_year": 2010,
            "genre": "Sci-Fi",
            "rating": 8.8
        }
        self.user_data = {
            "name": "John Doe",
            "email": "john@example.com"
        }

    def test_add_movie(self):
        """Testing adding a movie to the library"""
        self.library.add_movie(self.movie_data)
        self.assertEqual(len(self.library.movies), 1)
        self.assertEqual(self.library.movies[0].get_movie_title(), "Inception")

    def test_remove_movie(self):
        """Testing removing a movie from the library"""
        self.library.add_movie(self.movie_data)
        self.library.remove_movie(self.movie_data['title'])
        self.assertEqual(len(self.library.movies), 0)

    def test_register_user(self):
        """Testing user registration in the system"""
        self.library.register_user(self.user_data)
        self.assertEqual(len(self.library.users), 1)
        self.assertEqual(self.library.users[0].get_user_name(), "John Doe")

    def test_track_viewing_status(self):
        """Testing tracking viewing status of a movie by a user"""
        self.library.register_user(self.user_data)
        self.library.add_movie(self.movie_data)

        # Manually add the movie to the user's collection
        user = self.library.users[0]
        movie = self.library.movies[0]
        user.add_movie(movie)

        # Now change the viewing status
        self.library.track_viewing_status("John Doe", "Inception", "Watched")

        # Check if the status was updated correctly
        status = user.get_viewing_status("Inception")
        self.assertEqual(status, "Watched")

    def test_search_movies_by_title(self):
        """Testing searching movies by title"""
        self.library.add_movie(self.movie_data)
        result = self.library.search_movies({"title": "Inception"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_movie_title(), "Inception")

    def test_search_movies_by_director(self):
        """Testing searching movies by director"""
        self.library.add_movie(self.movie_data)
        result = self.library.search_movies({"director": "Christopher Nolan"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_movie_director(), "Christopher Nolan")

    def test_search_movies_by_release_year(self):
        """Testing searching movies by release year"""
        self.library.add_movie(self.movie_data)
        result = self.library.search_movies({"release_year": 2010})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_release_year(), 2010)

    def test_search_movies_by_genre(self):
        """Testing searching movies by genre"""
        self.library.add_movie(self.movie_data)
        result = self.library.search_movies({"genre": "Sci-Fi"})
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_genre(), "Sci-Fi")

    def test_save_to_json(self):
        """Testing saving the library system to a JSON file"""
        self.library.add_movie(self.movie_data)
        self.library.register_user(self.user_data)
        self.library.save_to_json('test_library.json')
        with open('test_library.json', 'r', encoding='utf-8') as f:
            data = f.read()
        self.assertIn("Inception", data)
        self.assertIn("John Doe", data)

    def test_load_from_json(self):
        """Testing loading the library system from a JSON file"""
        self.library.add_movie(self.movie_data)
        self.library.register_user(self.user_data)
        self.library.save_to_json('test_library.json')

        new_library = MovieLibrarySystem()
        new_library.load_from_json('test_library.json')

        self.assertEqual(len(new_library.movies), 1)
        self.assertEqual(len(new_library.users), 1)
        self.assertEqual(new_library.movies[0].get_movie_title(), "Inception")
        self.assertEqual(new_library.users[0].get_user_name(), "John Doe")

if __name__ == '__main__':
    unittest.main()
