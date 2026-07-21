"""
user.py

Contains the User class.
"""

from models.person import Person


class User(Person):
    """Represents a system user."""

    # Class attribute for auto-generating IDs
    next_id = 1

    def __init__(self, name: str, email: str, user_id=None, projects=None):
        """Initialize a User object."""

        super().__init__(name, email)

        # Use existing ID when loading from JSON
        if user_id is None:
            self.id = User.next_id
            User.next_id += 1
        else:
            self.id = user_id

            # Keep next_id ahead of loaded IDs
            if user_id >= User.next_id:
                User.next_id = user_id + 1

        # Store project IDs
        self.projects = projects if projects else []

    def add_project(self, project_id: int):
        """Add a project to the user."""

        if project_id not in self.projects:
            self.projects.append(project_id)

    def remove_project(self, project_id: int):
        """Remove a project from the user."""

        if project_id in self.projects:
            self.projects.remove(project_id)

    def to_dict(self):
        """Convert User to a dictionary."""

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": self.projects,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a User from a dictionary."""

        return cls(
            name=data["name"],
            email=data["email"],
            user_id=data["id"],
            projects=data.get("projects", []),
        )

    def __str__(self):
        """Readable string representation."""

        return (
            f"User(ID={self.id}, "
            f"Name='{self.name}', "
            f"Projects={len(self.projects)})"
        )