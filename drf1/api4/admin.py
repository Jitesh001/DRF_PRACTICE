from django.contrib import admin
from .models import Student4

@admin.register(Student4)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')