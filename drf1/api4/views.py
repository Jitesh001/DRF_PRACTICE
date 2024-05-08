from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student4
from .serializers import StudentSerializer4
# sample apiview
# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({'msg':'Hello POST API', 'content':request.data})
#     return Response({'msg':'Hello GET API'})

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        if pk is not None:
            student = Student4.objects.get(id=pk)
            serializer = StudentSerializer4(student)
            return Response(serializer.data)
        
        students = Student4.objects.all()
        serializer = StudentSerializer4(students, many=True)
        return Response({'message':'Data Fetched', 'data':serializer.data})
    
    if request.method == 'POST':
        serializer = StudentSerializer4(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    #complete data update
    if request.method == 'PUT':
        #id = request.data.get('id')
        student = Student4.objects.get(id=pk)
        serializer = StudentSerializer4(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=201)
        return Response(serializer.errors, status=400)
    
    #partial data update
    if request.method == 'PATCH':
        #id = request.data.get('id')
        student = Student4.objects.get(id=pk)
        serializer = StudentSerializer4(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=201)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        #id = request.data.get('id')
        student = Student4.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted successfully'})