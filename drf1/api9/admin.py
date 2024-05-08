from django.contrib import admin
from .models import Student9, Teacher9, Product

@admin.register(Student9)  #method to display only required field
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')

@admin.register(Teacher9)  #method to display only required field
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'city') 


@admin.register(Product)  #method to display only required field
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')