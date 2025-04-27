from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Task
from .serializers import TaskSerializer
from django.shortcuts import get_object_or_404

# Creating a new task
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task_api(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Updating an existing task
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_task_api(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    serializer = TaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Deleting an existing task
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_task_api(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)