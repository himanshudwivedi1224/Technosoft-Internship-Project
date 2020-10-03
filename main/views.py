from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Classroom
from .models import Course
from .models import Student
from .models import Course_running

def index(request):
    return render(request,'main/index.html')

def classroom(request):
    print("Inside classroom")
    model_classroom = Classroom()
    if request.method == 'POST':
        print("request.method ==")
        model_classroom.Floor = request.POST['Floor']
        model_classroom.room_number = request.POST['room_number']
        model_classroom.capacity = request.POST['capacity']
        print(model_classroom.Floor)
        print(model_classroom.save())
        return render(request,'main/thankyou.html')
    return render(request, 'main/classroom.html')

    
def course(request):
    model_course = Course()
    if request.method == 'POST':
        print("request.method ==")
        model_course.title = request.POST['title']
        model_course.credit = request.POST['credit']
        print(model_course.title)
        print(model_course.save())
        return render(request,'main/thankyou.html')
    return render(request,'main/course.html')

def student(request):
    model_student = Student()
    if request.method == 'POST':
        print("request.method ==")
        model_student.id = '1'
        model_student.name = request.POST['name']
        model_student.dept_name = request.POST['dept_name']
        model_student.salary = request.POST['salary']
        print(model_student.name)
        print(model_student.save())
        return render(request,'main/thankyou.html')
    return render(request,'main/student.html')

def course_running(request):
    model_course_running = Course_running()
    if request.method == 'POST':
        print("request.method ==")
        model_course_running.id = '1'
        model_course_running.name = request.POST['name']
        model_course_running.dept = request.POST['dept']
        model_course_running.fees = request.POST['fees']
        print(model_course_running.dept)
        return render(request,'main/thankyou.html')
    return render(request,'main/course_running.html')

def teaches(request):
    model_teaches = teaches()
    if request.method == 'POST':
        print("request.method ==")
        model_teaches.id = '1'
        model_teaches.Floor = request.POST['Floor']
        model_teaches.room_number = request.POST['room number']
        model_teaches.capacity = request.POST['capacity']
        print(model_teaches.Floor)
        print(model_teaches.save())
        return render(request,'main/thankyou.html')
    return render(request,'main/teaches.html')

def advisor(request):
    model_advisor = Advisor()
    if request.method == 'POST':
        print("request.method ==")
        model_advisor.id = '1'
        model_advisor.name = request.POST['name']
        model_advisor.dept = request.POST['dept']
        print(model_advisor.dept)
        return render(request,'main/thankyou.html')
    return render(request,'main/advise.html')
def section(request):
    return render(request,'main/section.html')
def timeslot(request):
    return render(request,'main/timeslot.html')
def echo(request):
    model_classroom = Classroom()
    all_datas = model_classroom.objects.all()
    print(model_classroom)
    return render(request,'main/echo.html' , {'Floor' : all_datas})
