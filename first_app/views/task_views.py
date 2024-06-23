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
        fields = '__all__'  # Или перечислите конкретные поля, которые вы хотите включить

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['subtasks'] = SubTaskSerializer(
            instance.subtask_set.all(), many=True
        ).data
        return representation
