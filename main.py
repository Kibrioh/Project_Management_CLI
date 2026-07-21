"""
main.py

Entry point for the Project Management CLI.
"""

import argparse

from models.user import User
from models.task import Task
from rich.table import Table
from rich.console import Console
from models.project import Project


from utils.storage import load_data, save_data

console = Console()


def main():
    """Configure and run the command-line interface."""

    parser = argparse.ArgumentParser(
        prog="ProjectCLI",
        description="Project Management CLI"
    )

    # Create subcommands
    subparsers = parser.add_subparsers(
        dest="command",
        help="Available commands"
    )

    # -------------------------
    # User Commands
    # -------------------------

    add_user = subparsers.add_parser(
        "add-user",
        help="Add a new user"
    )

    add_user.add_argument(
        "--name",
        required=True,
        help="User's full name"
    )

    add_user.add_argument(
        "--email",
        required=True,
        help="User's email address"
    )

    subparsers.add_parser(
        "list-users",
        help="List all users"
    )

    # -------------------------
    # Project Commands
    # -------------------------

    add_project = subparsers.add_parser(
        "add-project",
        help="Add a new project"
    )

    add_project.add_argument(
        "--title",
        required=True,
        help="Project title"
    )

    add_project.add_argument(
        "--description",
        required=True,
        help="Project description"
    )

    add_project.add_argument(
        "--due-date",
        required=True,
        help="Due date (YYYY-MM-DD)"
    )

    add_project.add_argument(
        "--user-id",
        type=int,
        required=True,
        help="Owner's user ID"
    )

    subparsers.add_parser(
        "list-projects",
        help="List all projects"
    )

    add_task = subparsers.add_parser(
        "add-task",
        help="Add a task to a project"
    )

    add_task.add_argument(
        "--title",
        required=True,
        help="Task title"
    )

    add_task.add_argument(
        "--project-id",
        type=int,
        required=True,
        help="Project ID"
    )

    add_task.add_argument(
        "--assigned-to",
        type=int,
        required=True,
        help="Assigned user ID"
    )

    subparsers.add_parser(
        "list-tasks",
        help="List all tasks"
    )

    args = parser.parse_args()

    if args.command == "add-user":

        users = load_data("users.json", User)

        user = User(
            name=args.name,
            email=args.email
        )

        users.append(user)

        save_data("users.json", users)

        console.print("[bold green]✓ User added successfully[/bold green]")


    elif args.command == "list-users":

        users = load_data("users.json", User)

        if not users:
            print("No users found.")
            
        else:
            table = Table(title="Users")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Email", style="magenta")
            table.add_column("Projects", justify="center")

            for user in users:

                table.add_row(
                    str(user.id),
                    user.name,
                    user.email,
                    str(len(user.projects))
                )

            console.print(table)

    elif args.command == "add-project":

        users = load_data("users.json", User)
        projects = load_data("projects.json", Project)

        # Verify the user exists
        user = next((u for u in users if u.id == args.user_id), None)

        if user is None:
            print("User not found.")
            return

        project = Project(
            title=args.title,
            description=args.description,
            due_date=args.due_date,
            user_id=args.user_id
        )

        projects.append(project)

        # Link project to user
        user.add_project(project.id)

        save_data("projects.json", projects)
        save_data("users.json", users)

        console.print("[bold green]✓ Project updated successfully[/bold green]")


    elif args.command == "list-projects":
        projects = load_data("projects.json", Project)

        if not projects:
            print("No projects found.")

        else:
            table = Table(title="Projects")
            table.add_column("ID", style="cyan")
            table.add_column("Title", style="green")
            table.add_column("Owner")
            table.add_column("Due Date")
            table.add_column("Tasks")

            for project in projects:

                table.add_row(
                    str(project.id),
                    project.title,
                    str(project.user_id),
                    project.due_date,
                    str(len(project.tasks))
                )

            console.print(table)


    elif args.command == "add-task":
        users = load_data("users.json", User)
        projects = load_data("projects.json", Project)
        tasks = load_data("tasks.json", Task)

        # Verify assigned user exists
        assigned_user = next(
            (u for u in users if u.id == args.assigned_to),
            None
        )

        if assigned_user is None:
            print("Assigned user not found.")
            return

        # Verify project exists
        project = next(
            (p for p in projects if p.id == args.project_id),
            None
        )

        if project is None:
            print("Project not found.")
            return

        task = Task(
            title=args.title,
            assigned_to=args.assigned_to,
            project_id=args.project_id
        )

        tasks.append(task)

        # Link task to project
        project.add_task(task.id)

        save_data("tasks.json", tasks)
        save_data("projects.json", projects)

        print(f"Task '{task.title}' added successfully.")

    elif args.command == "list-tasks":

        tasks = load_data("tasks.json", Task)

        if not tasks:
            print("No tasks found.")

        else:
            table = Table(title="Tasks")

            table.add_column("ID", style="cyan")
            table.add_column("Title", style="green")
            table.add_column("Status")
            table.add_column("Assigned To")
            table.add_column("Project")

            for task in tasks:

                table.add_row(
                    str(task.id),
                    task.title,
                    task.status,
                    str(task.assigned_to),
                    str(task.project_id)
                )

            console.print(table)

    elif args.command == "complete-task":

        tasks = load_data("tasks.json", Task)

        task = next(
            (t for t in tasks if t.id == args.task_id),
            None
        )

        if task is None:
            print("Task not found.")
            return

        task.mark_complete()

        save_data("tasks.json", tasks)

        print("Task marked as completed.")

    elif args.command == "update-project":

        projects = load_data("projects.json", Project)

        project = next(
            (p for p in projects if p.id == args.project_id),
            None
        )

        if project is None:
            print("Project not found.")
            return

        # Update only the supplied fields
        if args.title:
            project.title = args.title

        if args.description:
            project.description = args.description

        if args.due_date:
            project.due_date = args.due_date

        save_data("projects.json", projects)

        print("Project updated successfully.")

    elif args.command == "update-user":

        users = load_data("users.json", User)

        user = next(
            (u for u in users if u.id == args.user_id),
            None
        )

        if user is None:
            print("User not found.")
            return

        if args.name:
            user.name = args.name

        if args.email:
            user.email = args.email

        save_data("users.json", users)

        print("User updated successfully.")

    elif args.command == "update-task":

        tasks = load_data("tasks.json", Task)

        task = next(
            (t for t in tasks if t.id == args.task_id),
            None
        )

        if task is None:
            print("Task not found.")
            return

        if args.title:
            task.title = args.title

        if args.status:
            task.status = args.status

        save_data("tasks.json", tasks)

        print("Task updated successfully.")

# -------------------------
# Task Commands
# -------------------------

    

    complete_task = subparsers.add_parser(
        "complete-task",
        help="Mark a task as completed"
    )

    complete_task.add_argument(
        "--task-id",
        type=int,
        required=True,
        help="Task ID"
    )

    update_project = subparsers.add_parser(
    "update-project",
    help="Update a project's details"
    )

    update_project.add_argument(
        "--project-id",
        type=int,
        required=True,
        help="Project ID"
    )

    update_project.add_argument(
        "--title",
        help="New project title"
    )

    update_project.add_argument(
        "--description",
        help="New project description"
    )

    update_project.add_argument(
        "--due-date",
        help="New due date (YYYY-MM-DD)"
    )

    update_user = subparsers.add_parser(
    "update-user",
    help="Update a user's details"
)

    update_user.add_argument(
        "--user-id",
        type=int,
        required=True
    )

    update_user.add_argument(
        "--name"
    )

    update_user.add_argument(
        "--email"
    )

    update_task = subparsers.add_parser(
    "update-task",
    help="Update a task"
    )

    update_task.add_argument(
        "--task-id",
        type=int,
        required=True
    )

    update_task.add_argument(
        "--title"
    )

    update_task.add_argument(
        "--status"
    )



if __name__ == "__main__":
    main()