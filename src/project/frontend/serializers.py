from rest_framework import serializers
from .models import TaskModel

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("name", "duration", "deadline")
