from django.shortcuts import render
from rest_framework.response import Response
from .models import Student9, Teacher9, Product
from .serializers import StudentSerializer9, TeacherSerializer9, ProductSerializer
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from .customeperms import MyPermission
from .customeauth import CustomeAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle, ScopedRateThrottle
from api9.throttle import DeveloperThrottle

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student9.objects.all()
    serializer_class = StudentSerializer9 
    authentication_classes = [SessionAuthentication]
    #permission_classes = [DjangoModelPermissions]
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [AnonRateThrottle, DeveloperThrottle]
    
class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher9.objects.all()
    serializer_class = TeacherSerializer9 
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [MyPermission]
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'teacher'

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [MyPermission]
    # authentication_classes = [CustomeAuthentication]
    # permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]