from django.urls import path
from .views import create_task_api

urlpatterns = [
    path('create/', create_task_api, name='api_create_task'),
]
