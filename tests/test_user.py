"""
Tests for the User class.
"""

import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User."""

    def test_create_user(self):
        """User should be created correctly."""

        user = User(
            "Brian",
            "brian@gmail.com"
        )

        self.assertEqual(user.name, "Brian")
        self.assertEqual(user.email, "brian@gmail.com")
        self.assertEqual(user.projects, [])

    def test_add_project(self):
        """Project IDs should be added."""

        user = User(
            "Brian",
            "brian@gmail.com"
        )

        user.add_project(1)

        self.assertEqual(
            user.projects,
            [1]
        )

    def test_to_dict(self):
        """User converts to dictionary."""

        user = User(
            "Brian",
            "brian@gmail.com"
        )

        data = user.to_dict()

        self.assertEqual(
            data["name"],
            "Brian"
        )

        self.assertEqual(
            data["email"],
            "brian@gmail.com"
        )


if __name__ == "__main__":
    unittest.main()