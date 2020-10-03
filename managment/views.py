from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Destination
from .models import Person

def index(request):
    return render(request,'index.html')