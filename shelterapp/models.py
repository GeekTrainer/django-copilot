from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

# Create a shelter model with name, address, and phone number
class Shelter(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    email = models.EmailField(max_length=50)
    
    # Create a phone number field with a regular expression for the format of ###-###-####
    phone_regex = RegexValidator(regex=r'^\d{3}-\d{3}-\d{4}$', message="Phone number must be entered in the format: ###-###-####")
    phone_number = models.CharField(validators=[phone_regex], max_length=12)

    def __str__(self):
        return self.name

# Create a dog model with name, age, and a shelter
class Dog(models.Model):
    name = models.CharField(max_length=50)
    
    # Create an age field with validation for a minimum of 0 and a maximum of 20
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])

    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # Add get_absolute_url method to Dog model
    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={'pk': self.pk})
