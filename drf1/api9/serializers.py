from rest_framework import serializers
from .models import Student9, Teacher9, Product


class StudentSerializer9(serializers.ModelSerializer):
    class Meta:
        model = Student9
        fields = ['id','name', 'roll', 'city']

class TeacherSerializer9(serializers.ModelSerializer):
    class Meta:
        model = Teacher9
        fields = ['id','name', 'age', 'city']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name', 'price', 'category']


    