from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView

# Create your views here.
from todo.models import Task, Category


class HomePageView(TemplateView):
    template_name = 'todo/index.html'


class TaskListView(ListView):
    """
    view of list of tasks.
    """
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'all_task_list'

    def get_context_data(self, **kwargs):
        """
        :return: 2 query set for expired and not expired tasks.
        """
        context_data = super().get_context_data(**kwargs)
        context_data['ex_tasks'] = Task.objects.get_expired_task()
        context_data['not_ex_tasks'] = Task.objects.get_notexpired_task()
        return context_data


class TaskDetailView(DetailView):
    """
    view of detail of each task.
    """
    model = Task
    template_name = 'todo/task_detail.html'


class CategoryListView(ListView):
    """
    view of list of category.
    """
    model = Category
    template_name = 'todo/cat_list.html'
    context_object_name = 'all_category_list'

    def get_context_data(self, **kwargs):
        """
        :return: 2 query set for null of task category and not null of tasks category.
        """
        context_data = super().get_context_data(**kwargs)
        context_data['null_of_task'] = Category.objects.get_null_category()
        context_data['notnull_of_task'] = Category.objects.get_notnull_category()
        return context_data


class CategoryDetailView(DetailView):
    """
    view of detail of categoryes.
    """
    model = Category
    template_name = 'todo/cat_detail.html'


class TaskCreateView(CreateView):
    """
    view of creating task by crispy form design.
    """
    model = Task
    template_name = 'todo/task_new.html'
    fields = '__all__'
