from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('classroom', views.classroom, name='classroom'),
    path('course', views.course, name='course'),
    path('student', views.student, name='student'),
    path('course_running', views.course_running, name='course_running'),
    path('timeslot', views.timeslot, name='timeslot'),
    path('teaches', views.teaches, name='teaches'),
    path('advisor', views.advisor, name='advisor'),
    path('section', views.section, name='section'),
    path('echo', views.echo, name='echo'),
]
