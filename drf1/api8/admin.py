from django.contrib import admin
from .models import Student8

@admin.register(Student8)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')