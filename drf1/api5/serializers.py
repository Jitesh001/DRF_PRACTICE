from rest_framework import serializers
from .models import Student5

class StudentSerializer5(serializers.ModelSerializer):
    class Meta:
        model = Student5
        fields = ['id','name', 'roll', 'city']

    