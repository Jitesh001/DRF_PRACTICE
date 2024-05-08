from rest_framework import serializers
from .models import Student3

class StudentSerializer2(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    #user has no right to change this field
    class Meta:
        model = Student3
        fields = ['name', 'roll', 'city']

    # read_only_fields = ['name', 'roll']
    extra_kwargs = {'city':{'required':True}}
    #city field is required, else no POST req success

    #feild level validation
    def validate_roll(self, value):
        if value < 1:
            raise serializers.ValidationError("Roll number cannot be negative")
        return value