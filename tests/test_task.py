"""
Tests for Task.
"""

import unittest

from models.task import Task


class TestTask(unittest.TestCase):

    def test_default_status(self):

        task = Task(
            "Survey",
            1,
            1
        )

        self.assertEqual(
            task.status,
            "Pending"
        )

    def test_mark_complete(self):

        task = Task(
            "Survey",
            1,
            1
        )

        task.mark_complete()

        self.assertEqual(
            task.status,
            "Completed"
        )

    def test_status_validation(self):

        with self.assertRaises(ValueError):

            Task(
                "Survey",
                1,
                1,
                status="Done"
            )


if __name__ == "__main__":
    unittest.main()