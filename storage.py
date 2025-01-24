import json
import os
from task import Task

class Storage:
    FILE_PATH = os.path.join(os.getcwd(), "tasks.json")  # Dynamic file path

    @staticmethod
    def save_tasks(tasks):
        """Save tasks to a JSON file."""
        with open(Storage.FILE_PATH, "w") as file:
            json.dump([task.to_dict() for task in tasks], file)

    @staticmethod
    def load_tasks():
        """Load tasks from a JSON file."""
        try:
            with open(Storage.FILE_PATH, "r") as file:
                tasks_data = json.load(file)
                return [Task.from_dict(data) for data in tasks_data]
        except FileNotFoundError:
            print("⚠️  File not found. Starting with an empty task list.")
            return []
        except json.JSONDecodeError:
            print("⚠️  Corrupted JSON file. Resetting task list.")
            return []
