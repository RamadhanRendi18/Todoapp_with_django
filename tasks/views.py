from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm

    # if request.method == 'POST':
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')
    
    context = {'tasks' : tasks, 'form' : form}
    # return HttpResponse("Hello World")
    return render(request, 'tasks/list.html', context)

def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Ganti dengan nama URL yang sesuai
    context = {'form': form}
    return render(request, 'tasks/create_task.html', context)

def update_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update_task.html', {'form': form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)  
    if request.method == 'POST' :
        task.delete()
        return redirect('/')
    return render(request, 'tasks/delete_task.html', {'task': task})

