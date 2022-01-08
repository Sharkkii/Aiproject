import datetime
from enum import Enum
import numpy as np
import pandas as pd
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel, ReferenceTaskModel, RlAgentModel
from .serializers import TaskListSerializer, ReferenceTaskListSerializer, RlAgentSerializer
from django.http import JsonResponse
from .src.scheduler import JobScheduler

# Create your views here.

class Status(str, Enum):
    NONE = ""
    SUCCESS = "success"
    FAIL = "fail"

class ModelStatus(str, Enum):
    NONE = ""
    NEW = "new"
    MODIFIED = "modified"
    COMMITTED = "committed"

model = {
    "name": "",
    "status": ModelStatus.NONE
}
n_slot = -1
n_worker = -1
n_epoch = -1
n_train_eval = -1
n_test_eval = -1
job_scheduler = None

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
def deleteTask(request):

    name = request.data["name"]
    task = TaskModel.objects.get(pk=name)
    task.delete()
    response = Response()
    return response

@api_view(["POST"])
def initializeModel(request):

    global n_slot
    global n_worker
    global model
    global job_scheduler

    queryset = RlAgentModel.objects.filter(pk=request.data["name"])
    n_slot = int(request.data["n_slot"])
    n_worker = int(request.data["n_worker"])

    if (not queryset.exists()):

        job_scheduler = JobScheduler(
            n_slot = n_slot,
            n_worker = n_worker
        )
        job_scheduler.setup()

        model["name"] = request.data["name"]
        model["status"] = ModelStatus.NEW
        status = Status.SUCCESS

    else:
        status = Status.FAIL

    data = {
        "model_name": model["name"],
        "n_slot": n_slot,
        "n_worker": n_worker,
        "status": status,
        "model_status": model["status"]
    }   
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def trainModel(request):

    global n_epoch
    global n_train_eval
    global n_test_eval
    global model
    global job_scheduler

    n_epoch = int(request.data["n_epoch"])
    n_train_eval = int(request.data["n_train_eval"])
    n_test_eval = int(request.data["n_test_eval"])

    score = {
        "covered":[],
        "missed": []
    }

    if (job_scheduler is not None):
        train_score, test_score = job_scheduler.train(
            n_epoch = n_epoch,
            n_train_eval = n_train_eval,
            n_test_eval = n_test_eval,
            env_step = 1,
            dataset_size = 1000,
            batch_size = 100,
            return_score = True
        )

        score["covered"] = [ np.mean(score) for score in test_score["covered"] ]
        score["missed"] = [ np.mean(score) for score in test_score["missed"] ]
        
        if (model["status"] == ModelStatus.COMMITTED):
            model["status"] = ModelStatus.MODIFIED
        status = Status.SUCCESS
    
    else:
        status = Status.FAIL

    data = {
        "n_epoch": n_epoch,
        "n_train_eval": n_train_eval,
        "n_test_eval": n_test_eval,
        "covered": score["covered"],
        "missed": score["missed"],
        "model_name": model["name"],
        "status": status,
        "model_status": model["status"]
    }
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def loadModel(request):

    global n_slot
    global n_worker
    global model
    global job_scheduler

    queryset = RlAgentModel.objects.filter(pk=request.data["name"])

    if (queryset.exists()):

        entry = queryset.first()
        n_slot = entry.n_slot
        n_worker = entry.n_worker
        job_scheduler = JobScheduler(
            n_slot = n_slot,
            n_worker = n_worker
        )
        job_scheduler.setup()

        model["name"] = request.data["name"]
        job_scheduler.load(
            path_to_policy = "policy_" + model["name"],
            path_to_value = "value_" + model["name"],
            path_to_qvalue = "qvalue_" + model["name"]
        )

        model["status"] = ModelStatus.COMMITTED
        status = Status.SUCCESS

    else:
        status = Status.FAIL
    
    data = {
        "model_name": model["name"],
        "n_slot": n_slot,
        "n_worker": n_worker,
        "status": status,
        "model_status": model["status"]
    }
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def saveModel(request):

    global n_slot
    global n_worker
    global model
    global job_scheduler

    queryset = RlAgentModel.objects.filter(pk=model["name"])

    if (queryset.exists() and (model["status"] == ModelStatus.MODIFIED)):
        entry = queryset.first()
        entry.model_status = model["status"] = ModelStatus.COMMITTED
        entry.save()
        job_scheduler.save(
            path_to_policy = "policy_" + model["name"],
            path_to_value = "value_" + model["name"],
            path_to_qvalue = "qvalue_" + model["name"]
        )
        status = Status.SUCCESS
        
    elif ((not queryset.exists()) and (model["status"] == ModelStatus.NEW)):
        RlAgentModel.objects.create(
            name = model["name"],
            n_slot = n_slot,
            n_worker = n_worker,
            # env_name = ""
        )
        job_scheduler.save(
            path_to_policy = "policy_" + model["name"],
            path_to_value = "value_" + model["name"],
            path_to_qvalue = "qvalue_" + model["name"]
        )
        model["status"] = ModelStatus.COMMITTED
        status = Status.SUCCESS

    elif (model["status"] == ModelStatus.COMMITTED):
        status = Status.SUCCESS

    else:
        status = Status.FAIL
    
    data = {
        "model_name": model["name"],
        "status": status,
        "model_status": model["status"]
    }
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def getBestSchedule(request):

    global job_scheduler

    n_step = int(request.data["n_step"])
    n_sample = int(request.data["n_sample"])
    schedules = job_scheduler.get_best_schedule(
        n_step = n_step,
        n_sample = n_sample
    )

    data = pd.DataFrame(schedules).T
    data = data.to_dict()
    response = JsonResponse(data)
    return response
