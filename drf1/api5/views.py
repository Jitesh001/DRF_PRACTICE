from django.shortcuts import render
from rest_framework.response import Response
from .models import Student5
from .serializers import StudentSerializer5
from rest_framework.views import APIView

class StudentView5(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            student = Student5.objects.get(id=pk)
            serializer = StudentSerializer5(student)
            return Response(serializer.data)
        
        students = Student5.objects.all()
        serializer = StudentSerializer5(students, many=True)
        return Response({'message':'Data Fetched', 'data':serializer.data})
    
    def post(self, request, format=None):
        serializer = StudentSerializer5(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    #complete data update
    def put(self, request, pk=None, format=None):
        #id = request.data.get('id')
        student = Student5.objects.get(id=pk)
        serializer = StudentSerializer5(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=201)
        return Response(serializer.errors, status=400)
    
    #partial data update
    def patch(self, request, pk=None, format=None):
        #id = request.data.get('id')
        student = Student5.objects.get(id=pk)
        serializer = StudentSerializer5(instance=student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk=None, format=None):
        #id = request.data.get('id')
        student = Student5.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Data deleted successfully'})