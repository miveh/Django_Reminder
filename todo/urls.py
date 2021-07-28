from django.urls import path, include
from .views import TaskListView, HomePageView, TaskDetailView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('task_list/', TaskListView.as_view(), name='listview'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detailview')
]
