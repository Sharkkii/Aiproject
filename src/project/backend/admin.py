from django.contrib import admin
from .models import TaskModel, ReferenceTaskModel

# Register your models here.
admin.site.register(TaskModel)
admin.site.register(ReferenceTaskModel)