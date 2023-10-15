from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.http import JsonResponse

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'create_task.html')

def view_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'view_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('task_list')

def api_task_list(request):
    tasks = Task.objects.all()
    task_data = [{'title': task.title, 'description': task.description} for task in tasks]
    return JsonResponse({'tasks': task_data})