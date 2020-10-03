from django.db import models

# Create your models here.

class Destination(models.Model):

    id = models.AutoField(primary_key=True)
    city2 = models.CharField(max_length=100)
    course = models.TextField()
    marks1 = models.IntegerField()
    Budget = models.IntegerField()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()