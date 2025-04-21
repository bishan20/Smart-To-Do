from django.urls import path
from .views import create_task_api
from .views import edit_task_api
from .views import delete_task_api

urlpatterns = [
    path('create/', create_task_api, name='api_create_task'),
    path('tasks/<int:task_id>/edit/', edit_task_api, name='api_edit_task'),
    path('delete/<int:task_id>/', delete_task_api, name='api_delete_task'),

]
