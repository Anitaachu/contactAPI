from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=200)
    birthday = models.DateField(max_length=100)
    

    def __str__(self):
        return self.first_name