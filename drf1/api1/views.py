from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

#single student data
def student_detail(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    jsonData = JSONRenderer().render(serializer.data)
    return HttpResponse(jsonData, content_type='application/json')

#list of students
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    jsonData = JSONRenderer().render(serializer.data)
    print(stu, serializer, serializer.data)
    return HttpResponse(jsonData, content_type='application/json')