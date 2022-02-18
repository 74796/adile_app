from django.shortcuts import render
from django.utils import timezone
from .models import TodoTask


def task_list(request):
    tasks = TodoTask.objects.filter(deadline_time__gt=timezone.now()).order_by('created_at')
    return render(request, 'todo_list/task_list.html', {'tasks': tasks})
