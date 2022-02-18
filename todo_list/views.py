from django.shortcuts import render

# Create your views here.


def task_list(request):
    return render(request, 'todo_list/task_list.html', {})
