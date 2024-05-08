from rest_framework import serializers
from .models import Student6


class StudentSerializer6(serializers.ModelSerializer):
    class Meta:
        model = Student6
        fields = ['id','name', 'roll', 'city']

    