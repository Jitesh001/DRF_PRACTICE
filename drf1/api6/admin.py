from django.contrib import admin
from .models import Student6

@admin.register(Student6)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')