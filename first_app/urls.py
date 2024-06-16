from django.urls import path
from first_app.views.task_views import TaskCreateView, TaskListView
from first_app.views.statistics_views import TaskStatisticsView

urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),
]
