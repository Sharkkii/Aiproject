from django.urls import path
from . import views

urlpatterns = [
    path("get-task-list", views.getTaskList),
    path("get-reference-task-list", views.getReferenceTaskList),
    path("create-task", views.createTask),
    path("create-reference-task", views.createReferenceTask),
    path("delete-task", views.deleteTask),
    path("schedule-job", views.scheduleJob)
]