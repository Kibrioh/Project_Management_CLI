"""
storage.py

Provides utility functions for saving and loading
application data from JSON files.
"""

import json
from pathlib import Path


# Directory containing all JSON files
DATA_DIR = Path("data")


def load_data(filename: str, model_class):
    """
    Load objects from a JSON file.

    Args:
        filename (str): Name of the JSON file.
        model_class: Class used to recreate objects.

    Returns:
        list: List of model objects.
    """

    filepath = DATA_DIR / filename

    # Return an empty list if the file does not exist
    if not filepath.exists():
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        return [model_class.from_dict(item) for item in data]

    except json.JSONDecodeError:
        print(f"Warning: {filename} contains invalid JSON.")
        return []

    except Exception as error:
        print(f"Error loading {filename}: {error}")
        return []


def save_data(filename: str, objects):
    """
    Save objects to a JSON file.

    Args:
        filename (str): Name of the JSON file.
        objects (list): List of model objects.
    """

    filepath = DATA_DIR / filename

    # Create the directory if it doesn't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(
                [obj.to_dict() for obj in objects],
                file,
                indent=4,
            )

    except Exception as error:
        print(f"Error saving {filename}: {error}")