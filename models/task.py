"""
task.py

Contains the Task class.
"""


class Task:
    """Represents a project task."""

    # Auto-increment task IDs
    next_id = 1

    # Allowed task statuses
    VALID_STATUSES = ("Pending", "In Progress", "Completed")

    def __init__(
        self,
        title: str,
        assigned_to: int,
        project_id: int,
        status="Pending",
        task_id=None,
    ):
        """Initialize a Task."""

        if task_id is None:
            self.id = Task.next_id
            Task.next_id += 1
        else:
            self.id = task_id

            # Keep next_id ahead of loaded IDs
            if task_id >= Task.next_id:
                Task.next_id = task_id + 1

        self.title = title
        self.assigned_to = assigned_to
        self.project_id = project_id
        self.status = status

    @property
    def title(self):
        """Return task title."""
        return self._title

    @title.setter
    def title(self, value):
        """Validate task title."""
        if not value.strip():
            raise ValueError("Task title cannot be empty.")
        self._title = value

    @property
    def status(self):
        """Return task status."""
        return self._status

    @status.setter
    def status(self, value):
        """Validate task status."""
        if value not in Task.VALID_STATUSES:
            raise ValueError(
                f"Status must be one of {Task.VALID_STATUSES}"
            )
        self._status = value

    def mark_complete(self):
        """Mark the task as completed."""
        self.status = "Completed"

    def to_dict(self):
        """Convert Task to a dictionary."""

        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_id": self.project_id,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task from a dictionary."""

        return cls(
            title=data["title"],
            assigned_to=data["assigned_to"],
            project_id=data["project_id"],
            status=data["status"],
            task_id=data["id"],
        )

    def __str__(self):
        """Readable string representation."""

        return (
            f"Task(ID={self.id}, "
            f"Title='{self.title}', "
            f"Status='{self.status}')"
        )