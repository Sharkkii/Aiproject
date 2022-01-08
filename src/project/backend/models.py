from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    required_effort = models.FloatField()
    remaining_time = models.FloatField()

class ReferenceTaskModel(models.Model):
    name = models.CharField(max_length = 20, primary_key = True)
    slot = models.IntegerField()
    required_effort = models.FloatField()
    remaining_time = models.FloatField()
    P = models.FloatField()

class RlAgentModel(models.Model):
    name = models.CharField(max_length = 40, primary_key = True)
    n_slot = models.IntegerField()
    n_worker = models.IntegerField()
    env_name = models.CharField(max_length = 40)
