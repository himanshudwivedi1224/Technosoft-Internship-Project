from django.contrib import admin
from .models import Destination
from .models import Person


# Register your models here.
admin.site.register(Destination)
admin.site.register(Person)