from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., "Work", "Study", etc.
    
    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Associate task with a user
    title = models.CharField(max_length=255)  # Task name (e.g., "assignment")
    description = models.TextField(blank=True, null=True)  # Optional task description
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Optional category for task
    due_date = models.DateField()  # Deadline for the task
    priority = models.CharField(
        max_length=10,
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
        default='Medium'
    )
    completed = models.BooleanField(default=False)  # Mark task as completed or not
    created_at = models.DateTimeField(auto_now_add=True)  # Auto set the task creation time
    updated_at = models.DateTimeField(auto_now=True)  # Auto set when the task is last updated

    def __str__(self):
        return f"{self.title} - {self.user.username}"  # Show task name and owner
