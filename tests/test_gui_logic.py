import unittest
import os
from unittest.mock import MagicMock
from classes.user import User
from GUI_logic.sign_in_page import login
from GUI_logic.sign_up_page import register


class TestUserAuth(unittest.TestCase):

    def setUp(self):
        """Set up the environment before each test."""
        self.test_username = "test_user"
        self.test_email = "test_user@example.com"
        self.test_password = "123"  # Default password used in login function
        self.test_file = "users.json"  # Using default file to match the code

        # Ensure test file is empty or non-existent
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_register_new_user(self):
        """Test registering a new user and saving to JSON."""
        # Register a new user
        register(self.test_username, self.test_email, self.test_password)

        # Check if the user was saved correctly
        users = User.load_from_json(self.test_file)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].get_user_name(), self.test_username)
        self.assertEqual(users[0].get_email(), self.test_email)

    def test_login_success(self):
        """Test successful login with correct credentials."""
        # Register a test user first
        register(self.test_username, self.test_email, self.test_password)

        # Create a mock window to pass into login function
        mock_window = MagicMock()
        result = login(self.test_username, self.test_password, mock_window)

        # Check if login was successful
        self.assertTrue(result)
        mock_window.destroy.assert_called_once()  # Check that window was closed on successful login

    def test_login_failure(self):
        """Test login failure with incorrect credentials."""
        # Register a test user first
        register(self.test_username, self.test_email, self.test_password)

        # Create a mock window to pass into login function
        mock_window = MagicMock()
        result = login(self.test_username, "wrong_password", mock_window)

        # Check if login failed and window was not closed
        self.assertIsNone(result)
        mock_window.destroy.assert_not_called()


if __name__ == "__main__":
    unittest.main()
