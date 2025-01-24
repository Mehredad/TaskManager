from storage import Storage
from task import Task

class TaskManager:
    def __init__(self):
        """Initialize the TaskManager with an empty task list."""
        self.tasks = []

    def load_tasks(self):
        """Load tasks from storage."""
        self.tasks = Storage.load_tasks()

    def save_tasks(self):
        """Save tasks to storage."""
        Storage.save_tasks(self.tasks)

    def add_task(self, title, description, phase, priority, deadline=None):
        """Add a new task."""
        task = Task(title, description, phase, priority, deadline)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, task_id):
        """Delete a task by its ID."""
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        return len(self.tasks) < initial_length

    def mark_task_completed(self, task_id):
        """Mark a task as completed by its ID."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_completed()
                self.save_tasks()
                return True
        return False

    def list_tasks(self):
        """Return a list of all tasks."""
        return self.tasks

    def add_feedback(self, task_id, feedback):
        """Add feedback to a specific task."""
        for task in self.tasks:
            if task.id == task_id:
                task.add_feedback(feedback)
                self.save_tasks()
                return True
        return False
