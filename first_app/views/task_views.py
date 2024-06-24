from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import models
from django.utils.timezone import now
from first_app.models.task import Task
from first_app.serializers.task_serializers import TaskSerializer
from first_app.pagination import GlobalPagination


class TaskFilter(FilterSet):
    class Meta:
        model = Task
        fields = {
            'status': ['exact'],
            'deadline': ['gte', 'lte'],
        }


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = TaskFilter
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    pagination_class = GlobalPagination


class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskStatsView(APIView):
    def get(self, request, *args, **kwargs):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=models.Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=now()).count()

        status_counts_dict = {status['status']: status['count'] for status in status_counts}

        data = {
            'total_tasks': total_tasks,
            'status_counts': status_counts_dict,
            'overdue_tasks': overdue_tasks,
        }
        return Response(data)






"""

from rest_framework import generics, serializers
from ..models import Task
from ..serializers.task_serializers import TaskSerializer
from django_filters import rest_framework as filters
from first_app.models.pagination import CustomPageNumberPagination
from first_app.serializers.sub_task_serializers import SubTaskSerializer


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


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subtasks'] = SubTaskSerializer(
            instance.subtask_set.all(), many=True
        ).data
        return representation
"""