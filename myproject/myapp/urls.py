from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.view_task, name='view_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('api/tasks/', views.api_task_list, name='api_task_list'),
]