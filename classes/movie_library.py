import json
from classes.user import User  
from classes.movie import Movie 
from interfaces.movie_library import MovieLibrarySystemInterface

class MovieLibrarySystem(MovieLibrarySystemInterface):
    def __init__(self, movie_class: type, user_class: type):
        """Initialize the movie library system with injected dependencies.
        :param movie_class: The Movie class for creating movie objects.
        :param user_class: The User class for creating user objects.
        """
        self.movies = []  # List to store Movie objects
        self.users = []   # List to store User objects
        self.Movie = movie_class  # Injected Movie dependency
        self.User = user_class    # Injected User dependency

    def add_movie(self, movie_data: dict) -> None:
        """Adds a new movie to the collection."""
        movie = self.Movie.from_dict(movie_data)  # Injected Movie
        self.movies.append(movie)  # Append movie to the movies list

    def remove_movie(self, movie_id: int) -> None:
        """Removes a movie from the collection by its ID."""
        self.movies = [movie for movie in self.movies if movie.get_movie_title() != movie_id]  # Filter out the movie

    def register_user(self, user_data: dict) -> None:
        """Registers a new user in the system."""
        user = self.User.from_dict(user_data)  # Injected User
        self.users.append(user)  # Append user to the users list

    def track_viewing_status(self, user_id: str, movie_id: str, status: str) -> None:
        """Tracks the viewing status for a specific movie by a user."""
        for user in self.users:
            if user.get_user_name() == user_id:  # Find the user by name
                user.set_viewing_status(movie_id, status)  # Update the viewing status for the movie

    def search_movies(self, criteria: dict) -> list:
        """Searches for movies based on the criteria provided in the dictionary."""
        result = []
        for movie in self.movies:
            if (criteria.get("title") and criteria["title"].lower() in movie.get_movie_title().lower()) or \
               (criteria.get("director") and criteria["director"].lower() in movie.get_movie_director().lower()) or \
               (criteria.get("release_year") and criteria["release_year"] == movie.get_release_year()) or \
               (criteria.get("genre") and criteria["genre"].lower() in movie.get_genre().lower()):
                result.append(movie)
        return result

    def save_to_json(self, filename: str) -> None:
        """Saves the movie library system data to a JSON file."""
        data = {
            "movies": [movie.to_dict() for movie in self.movies],  # Convert all movies to dict
            "users": [user.to_dict() for user in self.users]       # Convert all users to dict
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filename: str) -> None:
        """Loads the movie library system data from a JSON file."""
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            self.movies = [self.Movie.from_dict(movie_data) for movie_data in data.get("movies", [])]  # Load movies
            self.users = [self.User.from_dict(user_data) for user_data in data.get("users", [])]       # Load users
