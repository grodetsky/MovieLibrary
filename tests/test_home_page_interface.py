import unittest
from unittest.mock import MagicMock
from GUI_interface.home_page import Home


class TestHomePageInterface(unittest.TestCase):

    def test_show_account_info(self):
        """Test the account info button click."""
        username = "test_user"
        home_page = Home(username)

        home_page.show_account_info()

    def test_show_movies_info(self):
        """Test the movies info button click."""
        username = "test_user"
        home_page = Home(username)

        home_page.show_movies_info()


if __name__ == "__main__":
    unittest.main()
