from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # List all tasks
    path('add/', views.add_task, name='add_task'),  # Add a new task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit an existing task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete a task
    path('base/', views.base_view, name='base_view'),  # URL to test base.html

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
