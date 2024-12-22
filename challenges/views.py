from django.shortcuts import render
from .models import Task
from django.views.generic import CreateView,ListView


class TaskCreateView(CreateView):
    model = Task
    template_name = "Tasks.html"


class TaskListView(ListView):
    model = Task
    template_name = "Tasks.html"
