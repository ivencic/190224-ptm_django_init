from rest_framework import generics
from first_app.models.task import Task
from first_app.serializers.task_serializers import TaskSerializer


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
