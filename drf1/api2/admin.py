from django.contrib import admin
from .models import Student2

@admin.register(Student2)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')