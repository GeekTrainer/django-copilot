# import path
from django.urls import path

# Import views
from . import views

# Create urlpatterns for the views
urlpatterns = [
    path('', views.DogListView.as_view(), name='dog_list'),
    path('<int:pk>/', views.DogDetailView.as_view(), name='dog_detail'),
    path('shelters/', views.ShelterListView.as_view(), name='shelter_list'),
    path('shelters/<int:pk>/', views.ShelterDetailView.as_view(), name='shelter_detail'),
]