from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView

# Create your views here.
from todo.models import Task, Category


class HomePageView(TemplateView):
    template_name = 'todo/index.html'


class TaskListView(ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'all_task_list'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class CategoryListView(ListView):
    model = Category
    template_name = 'todo/cat_list.html'
    context_object_name = 'all_category_list'

    # queryset = Category.objects.get_null_category()
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['null_of_task'] = Category.objects.get_null_category()
        context_data['notnull_of_task'] = Category.objects.get_notnull_category()
        return context_data


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'todo/cat_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/task_new.html'
    fields = '__all__'
