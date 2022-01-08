from rest_framework import serializers
from .models import TaskModel, ReferenceTaskModel, RlAgentModel

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("name", "remaining_time", "required_effort")

class ReferenceTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceTaskModel
        fields = ("name", "slot", "remaining_time", "required_effort", "P")

class RlAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RlAgentModel
        fields = ("name", "n_slot", "n_worker", "env_name")
