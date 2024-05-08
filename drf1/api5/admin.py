from django.contrib import admin
from .models import Student5

@admin.register(Student5)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')