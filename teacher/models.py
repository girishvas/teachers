from django.db import models
from django.utils import timezone


class Subject(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)

    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=180)
    last_name = models.CharField(max_length=180, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    phone_number = models.CharField(max_length=13)
    room_number = models.CharField(max_length=10)
    profile = models.ImageField(
        upload_to='profile', default='profile/default.jpg')
    subjects = models.ManyToManyField(Subject)

    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.first_name
