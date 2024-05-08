from django.shortcuts import render
from rest_framework.response import Response
from .models import Student8
from .serializers import StudentSerializer8
from rest_framework import status, viewsets

# Create your views here.
# class StudentViewset(viewsets.ViewSet):
#     def list(self, request):
#         stu = Student8.objects.all()
#         serializer = StudentSerializer8(stu, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StudentSerializer8(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         stu = Student8.objects.get(id=pk)
#         serializer = StudentSerializer8(stu)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         stu = Student8.objects.get(id=pk)
#         serializer = StudentSerializer8(instance=stu, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#ModelViewSet provide all the functions by default
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student8.objects.all()
    serializer_class = StudentSerializer8 

#ReadOnlyViewset implmentation
class StudentReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student8.objects.all()
    serializer_class = StudentSerializer8