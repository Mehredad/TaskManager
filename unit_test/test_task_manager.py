import unittest
from task_manager import TaskManager
from task import Task

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        """
        Set up a TaskManager instance and clear any existing tasks for testing.
        """
        self.task_manager = TaskManager()
        self.task_manager.tasks = []  # Clear any existing tasks

    def test_add_task(self):
        """
        Test adding a task to the task manager.
        """
        self.task_manager.add_task("Test Task", "Test Description", "Ideation", 3, "2024-12-31")
        self.assertEqual(len(self.task_manager.tasks), 1)  # Check if the task is added
        self.assertEqual(self.task_manager.tasks[0].title, "Test Task")  # Check task title

    def test_mark_task_completed(self):
        """
        Test marking a task as completed.
        """
        self.task_manager.add_task("Test Task", "Description", "Prototyping", 2, None)
        task_id = self.task_manager.tasks[0].id
        result = self.task_manager.mark_task_completed(task_id)
        self.assertTrue(result)  # Ensure the task was marked as completed
        self.assertTrue(self.task_manager.tasks[0].completed)  # Verify completion status

    def test_mark_task_completed_invalid_id(self):
        """
        Test marking a task as completed with an invalid ID.
        """
        result = self.task_manager.mark_task_completed("invalid-id")
        self.assertFalse(result)  # Ensure the result is False for an invalid ID

    def test_delete_task(self):
        """
        Test deleting a task.
        """
        self.task_manager.add_task("Test Task", "Description", "Testing", 4, None)
        task_id = self.task_manager.tasks[0].id
        result = self.task_manager.delete_task(task_id)
        self.assertTrue(result)  # Ensure the task was deleted
        self.assertEqual(len(self.task_manager.tasks), 0)  # Verify the task list is empty

    def test_delete_task_invalid_id(self):
        """
        Test deleting a task with an invalid ID.
        """
        result = self.task_manager.delete_task("invalid-id")
        self.assertFalse(result)  # Ensure the result is False for an invalid ID

    def test_add_feedback(self):
        """
        Test adding feedback to a task.
        """
        self.task_manager.add_task("Test Task", "Description", "Development", 5, None)
        task_id = self.task_manager.tasks[0].id
        result = self.task_manager.add_feedback(task_id, "Great work!")
        self.assertTrue(result)  # Ensure feedback was added
        self.assertIn("Great work!", self.task_manager.tasks[0].feedback)  # Check feedback content

    def test_add_feedback_invalid_id(self):
        """
        Test adding feedback to a task with an invalid ID.
        """
        result = self.task_manager.add_feedback("invalid-id", "Great work!")
        self.assertFalse(result)  # Ensure the result is False for an invalid ID

    def test_storage_save_and_load(self):
        """
        Test saving and loading tasks from storage.
        """
        self.task_manager.add_task("Test Task", "Description", "Development", 5, None)
        self.task_manager.save_tasks()  # Save tasks to JSON
        self.task_manager.load_tasks()  # Reload tasks from JSON
        self.assertEqual(len(self.task_manager.tasks), 1)  # Ensure the task is reloaded
        self.assertEqual(self.task_manager.tasks[0].title, "Test Task")  # Check task attributes

if __name__ == "__main__":
    unittest.main()
