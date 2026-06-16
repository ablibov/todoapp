from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Task.objects.create(
                title=title,
                description=description
            )

        return redirect('index')

    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def detail(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'detail.html', {'task': task})

def delete(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect('index')

def change_status(request, id):
    task = Task.objects.get(id=id)

    task.complited = not task.complited
    task.save()

    return redirect('/')