from rest_framework import serializers
from .models import Student4

class StudentSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Student4
        fields = ['id','name', 'roll', 'city']

    