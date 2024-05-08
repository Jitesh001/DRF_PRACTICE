from rest_framework import serializers
from .models import Student2

#validators funct
def name_length(name):
    if len(name) < 3:
        raise serializers.ValidationError("Name should be atleast 3 characters long")
    return name

class StudentSerializer2(serializers.Serializer):
    name =  serializers.CharField(max_length=100, validators=[name_length])
    roll = serializers.IntegerField()
    city  = serializers.CharField(max_length=100)

    def create(self, validate_data):
        return Student2.objects.create(**validate_data)
    
    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.roll = validate_data.get('roll', instance.roll)
        instance.city = validate_data.get('city', instance.city)
        instance.save()
        return instance
    
    #validations
    def validate_roll(self, value):
        if value < 1:
            raise serializers.ValidationError("Roll number cannot be negative")
        return value
    
    def validate(self, data):
        if not data.get('city').istitle():
            raise serializers.ValidationError("City name should be in title case")
        return data