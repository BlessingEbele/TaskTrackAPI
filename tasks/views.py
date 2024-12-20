# from django.shortcuts import render
# from rest_framework.test import APITestCase
# from rest_framework import status
# from tasks.models import Task

# class TaskAPITestCase(APITestCase):
#     def setUp(self):
#         self.task = Task.objects.create(
#             title="Learn Django Testing",
#             description="Learn how to write unit tests for Django apps.",
#             completed=False
#         )
#         self.task_url = "/api/tasks/"

#     def test_list_tasks(self):
#         response = self.client.get(self.task_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_task(self):
#         data = {"title": "New Task", "description": "Test task creation", "completed": False}
#         response = self.client.post(self.task_url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Task.objects.count(), 2)

#     def test_update_task(self):
#         url = f"{self.task_url}{self.task.id}/"
#         data = {"title": "Updated Task", "description": self.task.description, "completed": True}
#         response = self.client.put(url, data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.task.refresh_from_db()
#         self.assertTrue(self.task.completed)

#     def test_delete_task(self):
#         url = f"{self.task_url}{self.task.id}/"
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Task.objects.count(), 0)


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import permissions

# View for listing and creating tasks
class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the task
        serializer.save(user=self.request.user)

# View for retrieving, updating, and deleting a single task
class TaskDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
