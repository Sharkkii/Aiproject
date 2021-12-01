from django.views.generic import TemplateView
from .serializers import TaskListSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TaskModel

# Create your views here.

@api_view()
def getTaskList(request):
    data = TaskModel.objects.all()
    serializer = TaskListSerializer(data, many=True)
    response = Response(serializer.data)
    return response

class IndexView(TemplateView):
    template_name = "pages/index.html"
    serializer_class = TaskListSerializer
