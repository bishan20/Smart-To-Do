from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # List all tasks
    path('add/', views.add_task, name='add_task'),  # Add a new task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # Edit an existing task
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Delete a task

    path('tasks/<int:task_id>/toggle/', views.toggle_complete, name='toggle_complete'),
    path('dashboard/', views.dashboard, name='dashboard'), # Dashboard for tasks
    path('settings/', views.settings_view, name='settings'), # Settings to see user information
    path('settings/profile/', views.profile_view, name='profile'), # User profile
    path('settings/update/', views.update_profile, name='update_profile'), # Edit a user's profile

    path('base/', views.base_view, name='base_view'),  # URL to test base.html

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='tasks/password_change.html'), name='password_change'), # Changing a user's password
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='tasks/password_change_done.html'), name='password_change_done'), # Displaying flash message

    # Authentication URLs
    path('register/', views.register, name='register'), # Register a new user
    path('login/', views.user_login, name='login'), # Login an existing user
    path('logout/', views.user_logout, name='logout'), # Logout a user

    # Include API URLs
    path('api/', include('tasks.api.urls')), # All the APIs for tasks
]
