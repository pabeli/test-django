from django.shortcuts import render
from django.http import JsonResponse
from .models import TodoList


def index(request):
    all_todos = list(TodoList.objects.values())
    return JsonResponse(all_todos, safe=False, json_dumps_params={'indent': 2})

#def individual_get(request):
#    return HttpResponse('Hi, this is an individual post will be')
