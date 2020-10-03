from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
from .models import ClassRoom
from .models import Courseform
from .models import Departmentform
from .models import Insructorform
from .models import Prereq


def index(request):
    return render(request,'Createform/index.html')


def form(request):
    print("inside form action")
    return render(request,'Createform/form.html')

def classroom(request):
    model_classroom = classroom()
    if request.method == 'POST':
        print("request.method ==")
        model_classroom.id = '1'
        model_classroom.Building = request.POST['Building']
        model_classroom.room_number = request.POST['room number']
        model_classroom.capacity = request.POST['capacity']
        print(model_classroom.Building)
        print(model_classroom.save())
    return render(request,'Createform/form.html')

def Courseform(request):
    model_courseform = Courseform()
    if request.method == 'POST':
        print("request.method ==")
        model_courseform.id = '1'
        model_courseform.title = request.POST['title']
        model_courseform.credit = request.POST['credit']
        print(model_courseform.title)
        print(model_courseform.save())
    return render(request,'Createform/form.html')

def Departmentform(request):
    model_departmentform = Departmentform()
    if request.method == 'POST':
        print("request.method ==")
        model_departmentform.id = '1'
        model_departmentform.dept_name = request.POST['dept_name']
        model_departmentform.building = request.POST['building']
        model_departmentform.budget = request.POST['budget']
        print(model_departmentform.deptname)
        print(model_departmentform.save())
    return render(request,'Createform/form.html')

def instructorform(request):
    model_instructor = Insructorform()
    if request.method == 'POST':
        print("request.method ==")
        model_instructor.id = '1'
        model_instructor.name = request.POST['name']
        model_instructor.dept_name = request.POST['dept_name']
        print(model_instructor.name)
        print(model_instructor.save())
    return render(request,'Createform/form.html')

def Prereqform(request):
    model_prereq = Prereq()
    if request.method == 'POST':
        print("request.method ==")
        model_prereq.id = '1'
        model_prereq.prereqid = request.POST['prereq_id']
        model_prereq.courseid = request.POST['course_id']
        print(model_prereq.prereqid)
        print(model_prereq.save())
    return render(request,'Createform/form.html')