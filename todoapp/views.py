from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def home(request):

    task = Task.objects.all().order_by('-date')
    total_task = task.count()
    completed_task = Task.objects.filter(status=True).count()
    uncompleted_task = total_task - completed_task

    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home_view')


    context = {
        'task' : task,
        'total_task' : total_task,
        'completed_task' : completed_task,
        'uncompleted_task' : uncompleted_task,
        'form' : form
    }

    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def edit(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskEditForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('home_view')

    context = {
        'form' : form,
    }
    return render(request, 'edit.html', context)

def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        task.delete()
        return redirect("home_view")
    
    context = {
        'task': task
    }
    return render(request, 'delete.html', context)
