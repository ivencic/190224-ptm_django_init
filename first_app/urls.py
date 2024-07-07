from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from first_app.views.task_views import TaskListCreateView, TaskDetailUpdateDeleteView, TaskStatsView
from first_app.views.subtask_views import (
    SubTaskListView,
    SubTaskCreateView,
    SubTaskUpdateView,
    SubTaskDeleteView,
    SubTaskDetailView,
)
from first_app.views.category_views import CategoryViewSet


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('tasks/statistics/', TaskStatsView.as_view(), name='task-statistics'),

    path('subtasks/', SubTaskListView.as_view(), name='subtask-list-view'),
    path('subtasks/', SubTaskCreateView.as_view(), name='subtask-create-view'),
    path('subtasks/', SubTaskUpdateView.as_view(), name='subtask-update-view'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail-view'),
    path('subtasks/<int:pk>/', SubTaskDeleteView.as_view(), name='subtask-delete-view'),


    path('', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

"""
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
"""
