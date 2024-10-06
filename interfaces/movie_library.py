from abc import ABC, abstractmethod


class MovieLibrarySystemInterface(ABC):
    @abstractmethod
    def add_movie(self, movie_data: dict) -> None:
        """Adds a new movie to the collection."""
        pass

    @abstractmethod
    def remove_movie(self, movie_id: int) -> None:
        """Removes a movie from the collection."""
        pass

    @abstractmethod
    def register_user(self, user_data: dict) -> None:
        """Registers a new user in the system."""
        pass

    @abstractmethod
    def track_viewing_status(self, user_id: int, movie_id: int, status: str) -> None:
        """Tracks the viewing status for a specific movie."""
        pass

    @abstractmethod
    def search_movies(self, criteria: dict) -> list:
        """Searches for movies based on the criteria."""
        pass
