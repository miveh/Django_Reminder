from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.
from todo.models import Task


class HomePageView(TemplateView):
    template_name = 'todo/index.html'


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
