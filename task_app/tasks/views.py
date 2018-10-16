from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from tasks.models import Task
from tasks.forms import NewTaskForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required()
def tasks(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()
            new_task.author = request.user
            new_task.save()
    else:
        form = NewTaskForm()

    tasks = Task.objects.filter(author=request.user)
    return render(request, 'tasks.html', {'form': form, 'tasks': tasks})
