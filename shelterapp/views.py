from django.shortcuts import render

# Import ListView and DetailView from django.views.generic
from django.views.generic import ListView, DetailView

# Import models
from .models import Shelter, Dog

# Create your views here.

# Create a generic class view to list dogs
class DogListView(ListView):
    model = Dog
    template_name = 'dog_list.html'
    context_object_name = 'dogs'
    queryset = Dog.objects.all()

# Create a generic class view for dog details
class DogDetailView(DetailView):
    model = Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

# Create a generic class view to list shelters
class ShelterListView(ListView):
    model = Shelter
    template_name = 'shelter_list.html'
    context_object_name = 'shelters'
    queryset = Shelter.objects.all()

# Create a generic class view for shelter details
class ShelterDetailView(DetailView):
    model = Shelter
    template_name = 'shelter_detail.html'
    context_object_name = 'shelter'
