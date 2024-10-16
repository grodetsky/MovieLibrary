from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def get_user_name(self) -> str:
        """Returns the user's name."""
        pass

    @abstractmethod
    def get_email(self) -> str:
        """Returns the user's email."""
        pass

    @abstractmethod
    def get_added_movies(self) -> list:
        """Returns a list of movies added by the user."""
        pass

    @abstractmethod
    def get_viewing_status(self, movie_id: int) -> str:
        """Returns the viewing status for a specific movie."""
        pass
