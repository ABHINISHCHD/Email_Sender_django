from operator import mod
from django.db import models
from django.urls import reverse
# Create your models here.


class student(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)

    def get_absolute_url(self):
        return reverse('home')
    

    def __str__(self):
        return self.name


class staff(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    position=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    phone=models.IntegerField(max_length=10)

    def __str__(self):
        return self.name+' '+self.position

    