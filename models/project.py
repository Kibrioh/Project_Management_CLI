"""
project.py

Contains the Project class.
"""


class Project:
    """Represents a project."""

    # Auto-increment project IDs
    next_id = 1

    def __init__(
        self,
        title: str,
        description: str,
        due_date: str,
        user_id: int,
        project_id=None,
        tasks=None,
    ):
        """Initialize a Project."""

        if project_id is None:
            self.id = Project.next_id
            Project.next_id += 1
        else:
            self.id = project_id

            # Keep next_id ahead of loaded IDs
            if project_id >= Project.next_id:
                Project.next_id = project_id + 1

        self.title = title
        self.description = description
        self.due_date = due_date

        # Owner of the project
        self.user_id = user_id

        # Store task IDs
        self.tasks = tasks if tasks else []

    @property
    def title(self):
        """Return project title."""
        return self._title

    @title.setter
    def title(self, value):
        """Validate project title."""
        if not value.strip():
            raise ValueError("Project title cannot be empty.")
        self._title = value

    def add_task(self, task_id: int):
        """Add a task to the project."""

        if task_id not in self.tasks:
            self.tasks.append(task_id)

    def remove_task(self, task_id: int):
        """Remove a task from the project."""

        if task_id in self.tasks:
            self.tasks.remove(task_id)

    def to_dict(self):
        """Convert Project to a dictionary."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_id": self.user_id,
            "tasks": self.tasks,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Project from a dictionary."""

        return cls(
            title=data["title"],
            description=data["description"],
            due_date=data["due_date"],
            user_id=data["user_id"],
            project_id=data["id"],
            tasks=data.get("tasks", []),
        )

    def __str__(self):
        """Readable string representation."""

        return (
            f"Project(ID={self.id}, "
            f"Title='{self.title}', "
            f"Tasks={len(self.tasks)})"
        )