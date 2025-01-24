import uuid  # For generating unique task IDs
from datetime import datetime  # For handling task creation and deadlines

class Task:
    def __init__(self, title, description, phase, priority, deadline=None):
        """
        Initialize a Task object with title, description, phase, priority, and deadline.
        """
        self.id = str(uuid.uuid4())  # Generate a unique task ID
        self.title = title
        self.description = description
        self.phase = phase
        self.priority = priority
        self.deadline = deadline
        self.completed = False  # By default, tasks are not completed
        self.feedback = []  # Store feedback comments
        self.created_at = datetime.now()  # Timestamp for task creation

    def mark_as_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def add_feedback(self, feedback):
        """Add feedback to the task."""
        self.feedback.append(feedback)

    def to_dict(self):
        """Convert the task object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "phase": self.phase,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed,
            "feedback": self.feedback,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }

    @staticmethod
    def from_dict(data):
        """Reconstruct a Task object from a dictionary."""
        task = Task(data["title"], data["description"], data["phase"], data["priority"], data["deadline"])
        task.id = data["id"]
        task.completed = data["completed"]
        task.feedback = data["feedback"]
        task.created_at = datetime.strptime(data["created_at"], "%Y-%m-%d %H:%M:%S")
        return task
