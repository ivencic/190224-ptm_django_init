from django.urls import path
from first_app.views.task_views import TaskCreateView, TaskListView
from first_app.views.statistics_views import TaskStatisticsView
from first_app.views import subtask_views, task_views  # category_views


urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/statistics/', TaskStatisticsView.as_view(), name='task-statistics'),

    path('subtasks/', subtask_views.SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', subtask_views.SubTaskDetailUpdateDeleteView.as_view(),
         name='subtask-detail-update-delete'),

]