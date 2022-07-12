from django.contrib import admin

# Import the models
from .models import Shelter, Dog

# Register your models here.
admin.site.register(Shelter)
admin.site.register(Dog)
