from django.db import models

# Create your models here.


class MyUser(models.Model):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name