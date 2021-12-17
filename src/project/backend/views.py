import datetime
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel, ReferenceTaskModel
from .serializers import TaskListSerializer, ReferenceTaskListSerializer
from django.http import JsonResponse
from .src.scheduler import JobScheduler

# Create your views here.

scheduler = JobScheduler(
    n_slot = 3
)

@api_view(["GET"])
def getTaskList(request):
    
    data = TaskModel.objects.all()
    serializer = TaskListSerializer(data, many=True)
    response = Response(serializer.data)
    return response

@api_view(["GET"])
def getReferenceTaskList(request):

    data = ReferenceTaskModel.objects.all()
    serializer = ReferenceTaskListSerializer(data, many=True)
    response = Response(serializer.data)
    return response

@api_view(["POST"])
def createReferenceTask(request):
    
    task_name = request.data["name"]
    created_at = timezone.now().date()
    overdue_at = datetime.date.fromisoformat(request.data["remaining_time"])
    required_effort = request.data["required_effort"]
    
    ReferenceTaskModel.objects.create(
        name = task_name,
        created_at = created_at,
        overdue_at = overdue_at,
        remaining_time = (overdue_at - created_at).days,
        required_effort = required_effort
    )
    response = Response()
    return response

@api_view(["POST"])
def createTask(request):
    
    name = request.data["name"]
    task = ReferenceTaskModel.objects.get(pk=name)
    
    TaskModel.objects.create(
        name = task.name,
        created_at = task.created_at,
        overdue_at = task.overdue_at,
        remaining_time = (task.overdue_at - task.created_at).days,
        required_effort = task.required_effort
    )
    response = Response()
    return response

@api_view(["POST"])
def scheduleJob(request):

    n_step = int(request.data["n_step"])
    data = scheduler.schedule_job(
        n_step = n_step
    )
    response = JsonResponse(data)
    return response