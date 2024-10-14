import json
from interfaces.user import UserInterface
from classes.movie import Movie

class User(UserInterface):
    def __init__(self, name: str, email: str):
        """Initialize user attributes."""
        self.name = name
        self.email = email
        self.added_movies = {}  # Dictionary to store movies added by the user
        self.viewing_status = {}  # Dictionary to track viewing status of each movie

    def get_user_name(self) -> str:
        """Returns the user's name."""
        return self.name

    def get_email(self) -> str:
        """Returns the user's email."""
        return self.email

    def get_added_movies(self) -> list:
        """Returns a list of movies added by the user."""
        return list(self.added_movies.values())

    def get_viewing_status(self, movie_id: int) -> str:
        """Returns the viewing status for a specific movie."""
        return self.viewing_status.get(movie_id, "Not watched")  # Default status if not found

    def add_movie(self, movie) -> None:
        """Adds a movie to the user's collection."""
        self.added_movies[movie.get_movie_title()] = movie  # Store movie by title
        self.viewing_status[movie.get_movie_title()] = movie.get_viewing_status()  # Track status

    def set_viewing_status(self, movie_id: str, status: str) -> None:
        """Sets the viewing status for a specific movie."""
        if movie_id in self.added_movies:
            self.viewing_status[movie_id] = status  # Update status

    def to_dict(self) -> dict:
        """Converts the user object to a dictionary for JSON storage."""
        return {
            "name": self.name,
            "email": self.email,
            "added_movies": [movie.to_dict() for movie in self.added_movies.values()],  # Convert movies to dict
            "viewing_status": self.viewing_status
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Creates a user object from a dictionary (loading from JSON)."""
        user = cls(data["name"], data["email"])
        # Add movies to the user's collection
        for movie_data in data.get("added_movies", []):
            movie = Movie.from_dict(movie_data)  
            user.add_movie(movie)
            user.set_viewing_status(movie.get_movie_title(), movie_data.get("viewing_status", "Not watched"))
        return user

    @staticmethod
    def save_to_json(users: list, filename: str) -> None:
        """Saves a list of users to a JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([user.to_dict() for user in users], f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_json(filename: str) -> list:
        """Loads a list of users from a JSON file."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [User.from_dict(user_data) for user_data in data]
