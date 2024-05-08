from django.contrib import admin
from .models import Student3

@admin.register(Student3)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')