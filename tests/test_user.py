import unittest
from classes.user import User
from classes.movie import Movie


class TestUser(unittest.TestCase):

    def setUp(self):
        """Initialization before each test"""
        self.user = User("John Doe", "john@example.com")
        self.movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 8.8)
        self.user.add_movie(self.movie)  # Adding a movie to the user

    def test_get_user_name(self):
        """Testing user name retrieval"""
        self.assertEqual(self.user.get_user_name(), "John Doe")

    def test_get_email(self):
        """Testing user email retrieval"""
        self.assertEqual(self.user.get_email(), "john@example.com")

    def test_add_movie(self):
        """Testing adding a movie to the user"""
        new_movie = Movie("The Dark Knight", "Christopher Nolan", 2008, "Action", 9.0)
        self.user.add_movie(new_movie)
        added_movies = self.user.get_added_movies()
        self.assertEqual(len(added_movies), 2)  # Should be two movies
        self.assertEqual(added_movies[1].get_movie_title(), "The Dark Knight")

    def test_get_added_movies(self):
        """Testing retrieval of added movies"""
        added_movies = self.user.get_added_movies()
        self.assertEqual(len(added_movies), 1)
        self.assertEqual(added_movies[0].get_movie_title(), "Inception")

    def test_get_viewing_status(self):
        """Testing retrieval of movie viewing status"""
        status = self.user.get_viewing_status(self.movie.get_movie_title())
        self.assertEqual(status, "Not watched")  # Default status is "Not watched"

    def test_set_viewing_status(self):
        """Testing updating the viewing status of a movie"""
        self.user.set_viewing_status(self.movie.get_movie_title(), "Watched")
        status = self.user.get_viewing_status(self.movie.get_movie_title())
        self.assertEqual(status, "Watched")

    def test_to_dict(self):
        """Testing serialization of the user to a dictionary"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['name'], "John Doe")
        self.assertEqual(user_dict['email'], "john@example.com")
        self.assertEqual(len(user_dict['added_movies']), 1)
        self.assertEqual(user_dict['added_movies'][0]['title'], "Inception")

    def test_from_dict(self):
        """Testing creation of a User object from a dictionary"""
        user_data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "added_movies": [
                {
                    "title": "The Dark Knight",
                    "director": "Christopher Nolan",
                    "release_year": 2008,
                    "genre": "Action",
                    "rating": 9.0,
                    "viewing_status": "Watched"
                }
            ],
            "viewing_status": {
                "The Dark Knight": "Watched"
            }
        }
        user = User.from_dict(user_data)
        self.assertEqual(user.get_user_name(), "Jane Doe")
        self.assertEqual(user.get_email(), "jane@example.com")
        self.assertEqual(len(user.get_added_movies()), 1)
        self.assertEqual(user.get_added_movies()[0].get_movie_title(), "The Dark Knight")
        self.assertEqual(user.get_viewing_status("The Dark Knight"), "Watched")


if __name__ == '__main__':
    unittest.main()
