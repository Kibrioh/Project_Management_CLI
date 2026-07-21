"""
Tests for the Project class.
"""

import unittest

from models.project import Project


class TestProject(unittest.TestCase):

    def test_create_project(self):

        project = Project(
            "GIS",
            "Network Mapping",
            "2026-08-01",
            1
        )

        self.assertEqual(
            project.title,
            "GIS"
        )

        self.assertEqual(
            project.user_id,
            1
        )

    def test_add_task(self):

        project = Project(
            "GIS",
            "Mapping",
            "2026-08-01",
            1
        )

        project.add_task(10)

        self.assertEqual(
            project.tasks,
            [10]
        )

    def test_remove_task(self):

        project = Project(
            "GIS",
            "Mapping",
            "2026-08-01",
            1
        )

        project.add_task(2)

        project.remove_task(2)

        self.assertEqual(
            project.tasks,
            []
        )


if __name__ == "__main__":
    unittest.main()