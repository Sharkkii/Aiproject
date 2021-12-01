from django.db import models
from django.contrib.admin.widgets import AdminDateWidget

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length=20)
    duration = models.IntegerField()
    deadline = models.DateField()
