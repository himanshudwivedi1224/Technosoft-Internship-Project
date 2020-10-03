from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Person, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

class ClassRoom(models.Model):
    building = models.CharField(max_length=100)
    room_name = models.CharField(max_length=100)
    capacity = models.IntegerField()

class Courseform(models.Model):
    title = models.CharField(max_length=100)
    credit = models.IntegerField()

class Departmentform(models.Model):
    dept_name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    budget = models.IntegerField()

class Insructorform(models.Model):
    name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=100)
    salary = models.IntegerField()

class Prereq(models.Model):
    courseid = models.IntegerField()
    prereqid = models.IntegerField()
    