from django.db import models

# Create your models here.
class Singer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='song')
    duration = models.IntegerField()

    def __str__(self) -> str:
        return self.title