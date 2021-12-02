from rest_framework import serializers
from .models import TaskModel

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("id", "name", "created_at", "overdue_at", "remaining_time", "required_effort")
