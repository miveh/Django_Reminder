from django.urls import path, include
from .views import TaskListView, HomePageView, TaskDetailView, CategoryListView, CategoryDetailView, TaskCreateView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('task_list/', TaskListView.as_view(), name='listview'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detailview'),
    path('categories/', CategoryListView.as_view(), name='catlist'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='catdetail'),
    path('new/', TaskCreateView.as_view(), name='new_task'),
]
