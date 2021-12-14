import datetime
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel
from .serializers import TaskListSerializer
from django.http import JsonResponse

# Create your views here.

@api_view(["GET"])
def getTaskList(request):
    
    data = TaskModel.objects.all()
    serializer = TaskListSerializer(data, many=True)
    response = Response(serializer.data)
    return response

@api_view(["POST"])
def createTask(request):
    
    task_name = request.data["task_name"]
    created_at = timezone.now().date()
    overdue_at = datetime.date.fromisoformat(request.data["due"])
    required_effort = request.data["required_effort"]
    
    TaskModel.objects.create(
        name = task_name,
        created_at = created_at,
        overdue_at = overdue_at,
        remaining_time = (overdue_at - created_at).days,
        required_effort = required_effort
    )
    response = Response()
    return response
