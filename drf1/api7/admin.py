from django.contrib import admin
from .models import Student7

@admin.register(Student7)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')