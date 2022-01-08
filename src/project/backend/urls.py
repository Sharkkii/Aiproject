from django.urls import path
from . import views

urlpatterns = [
    path("get-reference-task-list", views.getReferenceTaskList),
    path("get-task-list", views.getTaskList),
    path("create-reference-task", views.createReferenceTask),
    path("create-task", views.createTask),
    path("delete-reference-task", views.deleteReferenceTask),
    path("delete-task", views.deleteTask),
    path("initialize-model", views.initializeModel),
    path("train-model", views.trainModel),
    path("load-model", views.loadModel),
    path("save-model", views.saveModel),
    path("get-best-schedule", views.getBestSchedule)
]