from rest_framework import serializers
from .models import Student8


class StudentSerializer8(serializers.ModelSerializer):
    class Meta:
        model = Student8
        fields = ['id','name', 'roll', 'city']

    