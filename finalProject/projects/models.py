from django.contrib.auth import get_user_model
from django.db import models

from finalProject.professionals.models import Professional

UserModel = get_user_model()

class Project(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='')
    location = models.CharField(max_length=100)
    expenses = models.FloatField()
    description = models.TextField()
    professional = models.ManyToManyField(Professional, blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
