from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.CharField(max_length=10)
    classroom = models.CharField(max_length=30)
    club = models.CharField(max_length=15)
    house = models.CharField(max_length=15)
    photo = models.FileField(default=None)

    def get_absolute_url(self):
        return reverse('students:student-index')
