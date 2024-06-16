from rest_framework import generics
from ..models import Task
from ..serializers.task_serializers import TaskSerializer
from django_filters import rest_framework as filters
from first_app.models.pagination import CustomPageNumberPagination


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'deadline': ['gte', 'lte'],
        }


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = TaskFilter
    pagination_class = CustomPageNumberPagination