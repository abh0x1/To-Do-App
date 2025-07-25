from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task
# def home(request):
#     return HttpResponse('<h1>Homepage</h1>')


def home(request):
    task = Task.objects.filter(is_completed=False).order_by('-updated_at')
    completed_task = Task.objects.filter(is_completed=True)

    context = {
        'tasks': task,
        'completed_tasks': completed_task
    }
    return render(request, 'home.html', context)
