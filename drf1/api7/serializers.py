from rest_framework import serializers
from .models import Student7


class StudentSerializer7(serializers.ModelSerializer):
    class Meta:
        model = Student7
        fields = ['id','name', 'roll', 'city']

    