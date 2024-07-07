from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from first_app.models.subtask import Subtask
from first_app.serializers.sub_task_serializers import SubTaskSerializer
from first_app.pagination import GlobalPagination
from first_app.permissions import IsAdmin, IsUser, IsGuest


class SubTaskCreateView(generics.CreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAdmin | IsUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SubTaskListView(generics.ListAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAdmin | IsUser | IsGuest]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['created_at']
    pagination_class = GlobalPagination


class SubTaskDetailView(generics.RetrieveAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAdmin | IsUser | IsGuest]


class SubTaskUpdateView(generics.UpdateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAdmin | IsUser]


class SubTaskDeleteView(generics.DestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAdmin]


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubTaskSerializer





########################### OLD CODE ###############################################


"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from first_app.models.subtask import Subtask
from first_app.serializers.sub_task_serializers import SubTaskSerializer
from django.shortcuts import get_object_or_404





class SubTaskListCreateView(APIView):
    def get(self, request):
        subtasks = Subtask.objects.all()
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubTaskDetailUpdateDeleteView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Subtask, pk=pk)

    def get(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk):
        subtask = self.get_object(pk)
        serializer = SubTaskSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subtask = self.get_object(pk)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""