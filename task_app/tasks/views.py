from django.shortcuts import render

from tasks.models import Task
from tasks.forms import NewTaskForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def tasks(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = NewTaskForm()

    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
