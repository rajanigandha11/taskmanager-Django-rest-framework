from django.urls import path
from . import views

from .views import TaskListCreateView, TaskDetailView, task_dashboard


urlpatterns = [
    path('', views.TaskListView.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/new/', views.TaskCreateView.as_view(), name='task-create'),
    path('task/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
]