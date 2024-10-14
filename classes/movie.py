import json
from interfaces.movie import MovieInterface

class Movie(MovieInterface):
    def __init__(self, title: str, director: str, release_year: int, genre: str, rating: float):
        """Initialize movie attributes"""
        self.title = title
        self.director = director
        self.release_year = release_year
        self.genre = genre
        self.rating = rating
        self.viewing_status = "Not watched"

    def get_movie_title(self) -> str:
        """Returns the title of the movie"""
        return self.title

    def get_movie_director(self) -> str:
        """Returns the director's name"""
        return self.director

    def get_release_year(self) -> int:
        """Returns the movie's release year"""
        return self.release_year

    def get_genre(self) -> str:
        """Returns the movie genre"""
        return self.genre

    def get_rating(self) -> float:
        """Returns the movie rating"""
        return self.rating

    def get_viewing_status(self) -> str:
        """Returns the viewing status (watched, queued, etc.)"""
        return self.viewing_status

    def set_viewing_status(self, status: str) -> None:
        """Changes the viewing status of the movie"""
        self.viewing_status = status

    def to_dict(self) -> dict:
        """Converts the movie object to a dictionary for JSON storage"""
        return {
            "title": self.title,
            "director": self.director,
            "release_year": self.release_year,
            "genre": self.genre,
            "rating": self.rating,
            "viewing_status": self.viewing_status
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a movie object from a dictionary (loading from JSON)"""
        movie = cls(
            data["title"],
            data["director"],
            data["release_year"],
            data["genre"],
            data["rating"]
        )
        movie.set_viewing_status(data.get("viewing_status", "Not watched"))  # Set default viewing status
        return movie

    @staticmethod
    def save_to_json(movies: list, filename: str) -> None:
        """Saves a list of movies to a JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([movie.to_dict() for movie in movies], f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> list:
        """Loads a list of movies from a JSON file"""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Movie.from_dict(movie_data) for movie_data in data]

