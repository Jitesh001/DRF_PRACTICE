from django.shortcuts import render
from .models import Student7
from .serializers import StudentSerializer7
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class StudentList(ListAPIView, CreateAPIView):
    queryset = Student7.objects.all()
    serializer_class = StudentSerializer7

class StudentUpdate(RetrieveUpdateDestroyAPIView):
    queryset = Student7.objects.all()
    serializer_class = StudentSerializer7