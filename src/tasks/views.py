from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Task
from .models import Category
from .forms import RegisterForm

# User registration view
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {"form": form})

# User login view
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('task_list')
        else:
            return render(request, 'tasks/login.html', {"error": "Invalid username or password"})
    return render(request, 'tasks/login.html')

# User logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Ensure only logged-in users can access tasks
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

# Add a new task (form-based view)
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority', 'Medium')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id) if category_id else None

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            due_date=due_date or None,
            priority=priority,
            category=category
        )
        return redirect('task_list')

    categories = Category.objects.all()
    return render(request, 'tasks/add_task.html', {'categories': categories})

# Edit an existing task
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.due_date = request.POST.get('due_date') or None
        task.priority = request.POST.get('priority', 'Medium')
        category_id = request.POST.get('category')
        task.category = Category.objects.get(id=category_id) if category_id else None
        task.save()
        return redirect('task_list')

    categories = Category.objects.all()
    return render(request, 'tasks/edit_task.html', {'task': task, 'categories': categories})

# Delete a task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')

# Base view
def base_view(request):
    return render(request, 'tasks/base.html')
