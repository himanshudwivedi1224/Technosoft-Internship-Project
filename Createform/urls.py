from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('classroom', views.classroom, name='classroom'),
    path('Courseform', views.Courseform, name='Courseform'),
    path('Departmentform', views.Departmentform, name='Departmentform'),
    path('instructorform', views.instructorform, name='instructorform'),
    path('Prereqform', views.Prereqform, name='Prereqform'), 
]