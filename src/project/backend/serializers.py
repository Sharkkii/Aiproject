from rest_framework import serializers
from .models import TaskModel, ReferenceTaskModel

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("id", "name", "created_at", "overdue_at", "remaining_time", "required_effort")

class ReferenceTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceTaskModel
        fields = ("id", "name", "created_at", "overdue_at", "remaining_time", "required_effort")