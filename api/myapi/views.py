from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from myapi.serializers import StudentSerializer
from myapi.models import Student


def studentview(request):
    stu=Student.objects.get(id=1)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type="application/json")
# Create your views here.
