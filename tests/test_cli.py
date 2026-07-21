"""
Unit tests for the CLI (main.py).
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys

from main import main


class TestCLI(unittest.TestCase):
    """Tests for the command-line interface."""

    @patch("main.save_data")
    @patch("main.load_data")
    def test_add_user(self, mock_load_data, mock_save_data):
        """Test adding a user through the CLI."""

        # Simulate an empty users list
        mock_load_data.return_value = []

        test_args = [
            "main.py",
            "add-user",
            "--name", "Brian",
            "--email", "brian@gmail.com"
        ]

        with patch.object(sys, "argv", test_args):
            main()

        # Ensure save_data() was called
        mock_save_data.assert_called_once()

    @patch("main.load_data")
    def test_list_users(self, mock_load_data):
        """Test listing users."""

        mock_load_data.return_value = []

        test_args = [
            "main.py",
            "list-users"
        ]

        with patch.object(sys, "argv", test_args):

            with patch("sys.stdout", new=StringIO()) as fake_output:

                main()

                self.assertIn(
                    "No users found",
                    fake_output.getvalue()
                )

    def test_invalid_command(self):
        """Test an invalid CLI command."""

        test_args = [
            "main.py",
            "invalid-command"
        ]

        with patch.object(sys, "argv", test_args):

            with self.assertRaises(SystemExit):

                main()


if __name__ == "__main__":
    unittest.main()