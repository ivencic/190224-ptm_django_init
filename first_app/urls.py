from django.urls import path
from first_app.views.task_views import TaskCreateView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
]
