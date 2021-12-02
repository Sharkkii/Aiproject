import datetime
from django.views.generic import TemplateView
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel
from .serializers import TaskListSerializer

# Create your views here.

@api_view(["GET"])
def getTaskList(request):
    
    data = TaskModel.objects.all()
    serializer = TaskListSerializer(data, many=True)
    response = Response(serializer.data)
    return response

class IndexView(TemplateView):
    template_name = "pages/index.html"
    serializer_class = TaskListSerializer
