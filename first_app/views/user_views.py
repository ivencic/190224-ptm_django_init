from rest_framework import generics
from first_app.models import Task
from first_app.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated


class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
