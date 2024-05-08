from django.db import models

#imports for creating Token using signal method
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Student9(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

class Teacher9(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=100)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    category = models.CharField(max_length=100)
    

# #function for creating token using signals
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#     #as user is created in USER model and after save this signal get invoked