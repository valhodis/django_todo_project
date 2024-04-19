from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'aplicatie/task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id, user=request.user)
    except Task.DoesNotExist:
        raise Http404("Taskul nu există sau nu aveți permisiunea să îl accesați.")
    return render(request, 'aplicatie/task_detail.html', {'task': task})


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'aplicatie/add_task.html', {'form': form})


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'aplicatie/update_task.html', {'form': form})


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'aplicatie/delete_task.html', {'task': task})


def complete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.completed = True
    task.save()
    return redirect('task_list')


def completed_tasks(request):
    completed_tasks_list = Task.objects.filter(completed=True)
    return render(request, 'aplicatie/completed_tasks.html', {'completed_tasks': completed_tasks_list})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
