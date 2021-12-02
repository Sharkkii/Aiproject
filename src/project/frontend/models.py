from django.db import models
from django.contrib.admin.widgets import AdminDateWidget
from django.utils import timezone

# Create your models here.
class TaskModel(models.Model):
    name = models.CharField(max_length = 20)
    required_effort = models.FloatField()
    remaining_time = models.FloatField()
    created_at = models.DateField(default=timezone.now)
    overdue_at = models.DateField()

