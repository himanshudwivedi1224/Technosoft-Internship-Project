from django.db import models

# Create your models here.

class Classroom(models.Model):
    Floor = models.CharField(max_length=100)
    room_number = models.IntegerField()
    capacity = models.IntegerField()

class Course(models.Model):
    title = models.CharField(max_length=100)
    credit = models.IntegerField()

class teaches(models.Model):
    Floor = models.CharField(max_length=100)
    room_number = models.IntegerField(default='01', editable=False)
    capacity = models.IntegerField()

class Course_running(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    fees = models.IntegerField(default='01', editable=True)

class Student(models.Model):
    name = models.CharField(max_length=100)
    dept_name = models.CharField(max_length=100)
    salary = models.IntegerField()
    
class Advisor(models.Model):
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)