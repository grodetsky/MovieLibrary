import unittest
import json
import os
from classes.movie import Movie

class TestMovie(unittest.TestCase):

    def setUp(self):
        """Initialization before each test"""
        self.movie = Movie("Inception", "Christopher Nolan", 2010, "Sci-Fi", 8.8)

    def test_get_movie_title(self):
        self.assertEqual(self.movie.get_movie_title(), "Inception")

    def test_get_movie_director(self):
        self.assertEqual(self.movie.get_movie_director(), "Christopher Nolan")

    def test_get_release_year(self):
        self.assertEqual(self.movie.get_release_year(), 2010)

    def test_get_genre(self):
        self.assertEqual(self.movie.get_genre(), "Sci-Fi")

    def test_get_rating(self):
        self.assertEqual(self.movie.get_rating(), 8.8)

    def test_set_viewing_status(self):
        self.movie.set_viewing_status("Watched")
        self.assertEqual(self.movie.get_viewing_status(), "Watched")

    def test_to_dict(self):
        expected_dict = {
            "title": "Inception",
            "director": "Christopher Nolan",
            "release_year": 2010,
            "genre": "Sci-Fi",
            "rating": 8.8,
            "viewing_status": "Not watched"
        }
        self.assertEqual(self.movie.to_dict(), expected_dict)

    def test_from_dict(self):
        movie_data = {
            "title": "The Dark Knight",
            "director": "Christopher Nolan",
            "release_year": 2008,
            "genre": "Action",
            "rating": 9.0,
            "viewing_status": "Watched"
        }
        movie = Movie.from_dict(movie_data)
        self.assertEqual(movie.get_movie_title(), "The Dark Knight")
        self.assertEqual(movie.get_movie_director(), "Christopher Nolan")
        self.assertEqual(movie.get_release_year(), 2008)
        self.assertEqual(movie.get_genre(), "Action")
        self.assertEqual(movie.get_rating(), 9.0)
        self.assertEqual(movie.get_viewing_status(), "Watched")

    def test_save_to_json(self):
        movies = [self.movie]
        Movie.save_to_json(movies, 'test_movies.json')
        with open('test_movies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(data[0]['title'], "Inception")
        self.assertEqual(data[0]['director'], "Christopher Nolan")
        self.assertEqual(data[0]['release_year'], 2010)
        self.assertEqual(data[0]['genre'], "Sci-Fi")
        self.assertEqual(data[0]['rating'], 8.8)
        os.remove('test_movies.json')  # delete the test file after the test

    def test_load_from_json(self):
        movie_data = [{
            "title": "Inception",
            "director": "Christopher Nolan",
            "release_year": 2010,
            "genre": "Sci-Fi",
            "rating": 8.8,
            "viewing_status": "Not watched"
        }]
        with open('test_movies.json', 'w', encoding='utf-8') as f:
            json.dump(movie_data, f, ensure_ascii=False, indent=4)
        movies = Movie.load_from_json('test_movies.json')
        self.assertEqual(len(movies), 1)
        self.assertEqual(movies[0].get_movie_title(), "Inception")
        print("Current working directory:", os.getcwd())
        os.remove('test_movies.json')  # delete the test file after the test

if __name__ == '__main__':
    unittest.main()
