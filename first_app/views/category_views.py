from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from first_app.models.category import Category
from first_app.serializers.category_serializers import CategorySerializer
from first_app.models.task import Task


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(category=category).count()
        return Response({'task_count': task_count})
