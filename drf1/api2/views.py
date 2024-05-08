from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer2
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student2 
#for class based views
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.
# @csrf_exempt
# def student_create(request):
#     if request.method == 'GET':
#         stu = Student2.objects.all()
#         serializer = StudentSerializer2(stu, many=True)
#         jsonData = JSONRenderer().render(serializer.data)
#         print(stu, serializer, serializer.data)
#         return HttpResponse(jsonData, content_type='application/json')
    
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         seriaziler = StudentSerializer2(data=pythondata)
#         if seriaziler.is_valid():
#             seriaziler.save()
#             res = {'Message': 'Data saved successfully'}
#             json_response = JSONRenderer().render(res)
#             return HttpResponse(json_response, content_type='application/json')
        
#         error = JSONRenderer().render(seriaziler.errors)
#         return HttpResponse(error, content_type='application/json')
    
#     if request.method == "PUT":
#         json_data = request.body 
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata['id']
#         stu = Student2.objects.get(id=id)
#         seriaziler = StudentSerializer2(stu, data=pythondata, partial=True)
#         # you can ommit "partial" param if you want to make full update mandatory
#         if seriaziler.is_valid():
#             seriaziler.save()
#             res = {'Message': 'Data updated successfully'}
#             json_response = JSONRenderer().render(res)
#             return HttpResponse(json_response, content_type='application/json')
        
#         error = JSONRenderer().render(seriaziler.errors)
#         return HttpResponse(error, content_type='application/json')
    
#     if request.method == "DELETE":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata['id']
#         try:
#             stu = Student2.objects.get(id=id)
#         except Exception as e:
#             return HttpResponse('Could not find student')
#         stu.delete()
#         res = {'Message': 'Data deleted successfully'}
#         json_response = JSONRenderer().render(res)
#         return HttpResponse(json_response, content_type='application/json')
    
#class based views
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self, request, *args, **kwargs):
        stu = Student2.objects.all()
        serializer = StudentSerializer2(stu, many=True)
        jsonData = JSONRenderer().render(serializer.data)
        print(stu, serializer, serializer.data)
        return HttpResponse(jsonData, content_type='application/json') 
    
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        seriaziler = StudentSerializer2(data=pythondata)
        if seriaziler.is_valid():
            seriaziler.save()
            res = {'Message': 'Data saved successfully'}
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')
        
        error = JSONRenderer().render(seriaziler.errors)
        return HttpResponse(error, content_type='application/json')
    
    def put(self, request, *args, **kwargs):
        json_data = request.body 
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata['id']
        stu = Student2.objects.get(id=id)
        seriaziler = StudentSerializer2(stu, data=pythondata, partial=True)
        # you can ommit "partial" param if you want to make full update mandatory
        if seriaziler.is_valid():
            seriaziler.save()
            res = {'Message': 'Data updated successfully'}
            json_response = JSONRenderer().render(res)
            return HttpResponse(json_response, content_type='application/json')
        
        error = JSONRenderer().render(seriaziler.errors)
        return HttpResponse(error, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata['id']
        try:
            stu = Student2.objects.get(id=id)
        except Exception as e:
            return HttpResponse('Could not find student')
        stu.delete()
        res = {'Message': 'Data deleted successfully'}
        json_response = JSONRenderer().render(res)
        return HttpResponse(json_response, content_type='application/json')