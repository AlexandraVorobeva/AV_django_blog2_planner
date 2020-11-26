from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def bd(request):
    tasks = Task.objects.all()
    return render(request, 'main/bd.html', {'title': 'Страница задач', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
