from abc import ABC, abstractmethod


class MovieInterface(ABC):
    @abstractmethod
    def get_movie_title(self) -> str:
        """Returns the title of the movie."""
        pass

    @abstractmethod
    def get_movie_director(self) -> str:
        """Returns the director's name."""
        pass

    @abstractmethod
    def get_release_year(self) -> int:
        """Returns the movie's release year."""
        pass

    @abstractmethod
    def get_genre(self) -> str:
        """Returns the movie genre."""
        pass

    @abstractmethod
    def get_rating(self) -> float:
        """Returns the movie rating."""
        pass

    @abstractmethod
    def get_viewing_status(self) -> str:
        """Returns the viewing status (watched, queued, etc.)."""
        pass
