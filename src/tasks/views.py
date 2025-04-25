from datetime import date, timedelta
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task, Category
from .forms import RegisterForm
from django.db.models import Case, When, IntegerField
from django.views.decorators.http import require_POST

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

    # Search functionality
    query = request.GET.get('search', '')
    if query:
        tasks = tasks.filter(title__icontains=query)

    # Sort functionality using Django ORM only
    sort = request.GET.get('sort', '')
    if sort == 'newest':
        tasks = tasks.order_by('-created_at')
    elif sort == 'oldest':
        tasks = tasks.order_by('created_at')
    elif sort == 'priority_high':
        tasks = tasks.annotate(
            priority_value=Case(
                When(priority='High', then=1),
                When(priority='Medium', then=2),
                When(priority='Low', then=3),
                default=4,
                output_field=IntegerField()
            )
        ).order_by('priority_value')
    elif sort == 'priority_low':
        tasks = tasks.annotate(
            priority_value=Case(
                When(priority='High', then=3),
                When(priority='Medium', then=2),
                When(priority='Low', then=1),
                default=2,
                output_field=IntegerField()
            )
        ).order_by('priority_value')
    elif sort == 'due_soon':
        tasks = tasks.order_by('due_date')
    elif sort == 'due_late':
        tasks = tasks.order_by('-due_date')

    # Filter functionality (Today’s Tasks and Upcoming Tasks)
    filter_type = request.GET.get('filter')
    today = timezone.localdate()
    upcoming = today + timedelta(days=7)

    if filter_type == 'today':
        tasks = tasks.filter(due_date=today)
    elif filter_type == 'upcoming':
        tasks = tasks.filter(due_date__range=[today, upcoming])

    # Pagination (always paginate the queryset)
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks/task_list.html', {
        'page_obj': page_obj,
        'sort': sort,
        'search': query,
        'today': today,
        'filter': filter_type,  # Pass the current filter for active state in the template
    })

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
        messages.success(request, "Task created successfully.")
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
        messages.success(request, "Task updated successfully.")
        return redirect('task_list')

    categories = Category.objects.all()
    return render(request, 'tasks/edit_task.html', {'task': task, 'categories': categories})

# Delete a task
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    messages.success(request, "Task deleted successfully.")
    return redirect('task_list')

@login_required
@require_POST
def toggle_complete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

@login_required
def dashboard(request):
    today = date.today()
    user_tasks = Task.objects.filter(user=request.user)

    stats = {
        'total': user_tasks.count(),
        'completed': user_tasks.filter(completed=True).count(),
        'due_today': user_tasks.filter(due_date=today).count(),
        'overdue': user_tasks.filter(due_date__lt=today, completed=False).count()
    }

    return render(request, 'tasks/dashboard.html', {'stats': stats})


# Base view
def base_view(request):
    return render(request, 'tasks/base.html')
