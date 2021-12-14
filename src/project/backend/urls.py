from django.urls import path
from . import views

urlpatterns = [
    path("get-task-list", views.getTaskList),
    path("create-task", views.createTask)
]