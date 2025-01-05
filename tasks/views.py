from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import date, timedelta

# Home page
def index(request):
    return render(request, 'tasks/index.html')

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'Your account has been created!')
            return redirect('tasks') 
        else:
            messages.error(request, 'There was an error in the registration. Please check the form and try again.')
    else:
        form = UserCreationForm()

    return render(request, 'tasks/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tasks')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'tasks/login.html', {'form': form})

# Logout view
@login_required
def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def tasks(request):
    user_tasks = Task.objects.filter(user=request.user)
    today_tasks = []
    scheduled_tasks = []

    for task in user_tasks:
        if task.due_date == date.today() and not task.completed:
            today_tasks.append(task)
        elif task.due_date > date.today() and not task.completed:
            scheduled_tasks.append(task)

    # Check conditions for display messages
    today_empty = not today_tasks
    scheduled_empty = not scheduled_tasks
    all_done_for_today = today_tasks and all(task.completed for task in today_tasks)

    return render(request, 'tasks/tasks.html', {
        'today_tasks': today_tasks,
        'scheduled_tasks': scheduled_tasks,
        'today_empty': today_empty,
        'scheduled_empty': scheduled_empty,
        'all_done_for_today': all_done_for_today
    })

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        repeat_daily = request.POST.get('repeat_daily') == 'on'

        # Create the task for today
        task = Task.objects.create(user=request.user, title=title, due_date=date.today(), repeat_daily=repeat_daily)

        return redirect('tasks')


@login_required
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.completed = True
    task.save()

    # If task is completed, create a new task for tomorrow
    if task.repeat_daily:
        tomorrow = date.today() + timedelta(days=1)
        Task.objects.create(user=request.user, title=task.title, due_date=tomorrow, repeat_daily=True)

    return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id, user=request.user)
    task.delete()
    return redirect('tasks')
