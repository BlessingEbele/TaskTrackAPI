from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from tasks.models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Write test cases",
            description="Test the application thoroughly.",
            completed=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Write test cases")
        self.assertEqual(self.task.description, "Test the application thoroughly.")
        self.assertFalse(self.task.completed)

    def test_string_representation(self):
        self.assertEqual(str(self.task), "Write test cases")
