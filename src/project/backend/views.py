import os
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

from backend.src.scheduler import JobScheduler
from backend.src.env import PATH_TO_ENV_CONFIG

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

env_name = ""
agent_name = ""
agent_status = ModelStatus.NONE
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
    
    ReferenceTaskModel.objects.create(
        name = request.data["name"],
        slot = request.data["slot"],
        remaining_time = request.data["remaining_time"],
        required_effort = request.data["required_effort"],
        P = request.data["P"]
    )
    response = Response()
    return response

@api_view(["POST"])
def createTask(request):
    
    task = ReferenceTaskModel.objects.get(pk=request.data["name"])
    
    TaskModel.objects.create(
        name = task.name,
        remaining_time = task.remaining_time,
        required_effort = task.required_effort
    )
    response = Response()
    return response

@api_view(["POST"])
def deleteReferenceTask(request):

    name = request.data["name"]
    task = ReferenceTaskModel.objects.get(pk=name)
    task.delete()
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
    global n_epoch
    global n_train_eval
    global n_test_eval
    global env_name
    global agent_name
    global agent_status
    global job_scheduler

    n_slot = int(request.data["n_slot"])
    n_worker = int(request.data["n_worker"])
    env_name = request.data["name"]
    agent_name = ""

    queryset = RlAgentModel.objects.filter(pk=env_name)
    data = pd.DataFrame(ReferenceTaskModel.objects.all().values())

    ext = ".csv"
    path = os.path.join(PATH_TO_ENV_CONFIG, env_name) + ext
    data.to_csv(path, index=False)

    if (not queryset.exists()):

        job_scheduler = JobScheduler(
            n_slot = n_slot,
            n_worker = n_worker
        )
        job_scheduler.setup(
            env_name = env_name
        )

        agent_status = ModelStatus.NEW
        status = Status.SUCCESS

    else:
        status = Status.FAIL

    data = {
        "n_slot": n_slot,
        "n_worker": n_worker,
        "env_name": env_name,
        "agent_name": agent_name,
        "agent_status": agent_status,
        "status": status,
    }   
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def trainModel(request):

    global n_slot
    global n_worker
    global n_epoch
    global n_train_eval
    global n_test_eval
    global env_name
    global agent_name
    global agent_status
    global job_scheduler

    n_epoch = int(request.data["n_epoch"])
    n_train_eval = int(request.data["n_train_eval"])
    n_test_eval = int(request.data["n_test_eval"])

    PATH_TO_DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "data"))
    ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ext = ".csv"

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
            dataset_size = 5000,
            batch_size = 50,
            return_score = True
        )

        score["covered"] = [ np.mean(score) for score in test_score["covered"] ]
        score["missed"] = [ np.mean(score) for score in test_score["missed"] ]
        
        df = pd.DataFrame(score)
        path = os.path.join(PATH_TO_DATA, ts) + ext
        df.to_csv(path, index=False)
        
        if (agent_status == ModelStatus.COMMITTED):
            agent_status = ModelStatus.MODIFIED
        status = Status.SUCCESS
    
    else:
        status = Status.FAIL

    data = {
        "n_epoch": n_epoch,
        "n_train_eval": n_train_eval,
        "n_test_eval": n_test_eval,
        "covered": score["covered"],
        "missed": score["missed"],
        "env_name": env_name,
        "agent_name": agent_name,
        "agent_status": agent_status,
        "status": status,
    }
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def loadModel(request):

    global n_slot
    global n_worker
    global n_epoch
    global n_train_eval
    global n_test_eval
    global env_name
    global agent_name
    global agent_status
    global job_scheduler

    queryset = RlAgentModel.objects.filter(pk=request.data["name"])

    data = pd.DataFrame(ReferenceTaskModel.objects.all().values())
    ext = ".csv"
    path = os.path.join(PATH_TO_ENV_CONFIG, env_name) + ext
    data.to_csv(path, index=False)

    if (queryset.exists()):

        entry = queryset.first()
        n_slot = entry.n_slot
        n_worker = entry.n_worker
        env_name = entry.env_name
        agent_name = request.data["name"]

        job_scheduler = JobScheduler(
            n_slot = n_slot,
            n_worker = n_worker
        )
        job_scheduler.setup(
            env_name = env_name
        )

        job_scheduler.load(
            path_to_policy = "policy_" + agent_name,
            path_to_value = "value_" + agent_name,
            path_to_qvalue = "qvalue_" + agent_name
        )

        agent_status = ModelStatus.COMMITTED
        status = Status.SUCCESS

    else:
        status = Status.FAIL
    
    data = {
        "n_slot": n_slot,
        "n_worker": n_worker,
        "env_name": env_name,
        "agent_name": agent_name,
        "agent_status": agent_status,
        "status": status,
    }
    response = JsonResponse(data)
    print(data)
    return response

@api_view(["POST"])
def saveModel(request):

    global n_slot
    global n_worker
    global n_epoch
    global n_train_eval
    global n_test_eval
    global env_name
    global agent_name
    global agent_status
    global job_scheduler

    agent_name = request.data["name"]
    queryset = RlAgentModel.objects.filter(pk=agent_name)

    if (queryset.exists() and (agent_status == ModelStatus.MODIFIED)):
        entry = queryset.first()
        entry.model_status = agent_status = ModelStatus.COMMITTED
        entry.save()
        job_scheduler.save(
            path_to_policy = "policy_" + agent_name,
            path_to_value = "value_" + agent_name,
            path_to_qvalue = "qvalue_" + agent_name
        )
        status = Status.SUCCESS
        
    else:
        RlAgentModel.objects.create(
            name = agent_name,
            n_slot = n_slot,
            n_worker = n_worker,
            env_name = env_name
        )
        job_scheduler.save(
            path_to_policy = "policy_" + agent_name,
            path_to_value = "value_" + agent_name,
            path_to_qvalue = "qvalue_" + agent_name
        )
        agent_status = ModelStatus.COMMITTED
        status = Status.SUCCESS
    
    data = {
        "env_name": env_name,
        "agent_name": agent_name,
        "agent_status": agent_status,
        "status": status,
    }
    response = JsonResponse(data)
    return response

@api_view(["POST"])
def getBestSchedule(request):

    global job_scheduler

    n_step = int(request.data["n_step"])
    n_sample = int(request.data["n_sample"])
    
    if (job_scheduler is not None):
        schedules = job_scheduler.get_best_schedule(
            n_step = n_step,
            n_sample = n_sample
        )
        data = pd.DataFrame(schedules).T
        data = data.to_dict()
    else:
        data = {}

    response = JsonResponse(data)
    return response

@api_view(["GET"])
def getExperimentalResult(request):

    name = request.query_params.get("name")
    print(name)
    
    PATH_TO_DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), "src", "data"))
    ext = ".csv"
    path = os.path.join(PATH_TO_DATA, name) + ext
    if (os.path.exists(path)):
        df = pd.read_csv(path)
        data = df.to_dict()
    else:
        data = {
            "covered": [],
            "missed": []
        }

    response = JsonResponse(data)
    return response
