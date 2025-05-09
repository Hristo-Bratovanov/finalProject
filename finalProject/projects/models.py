from django.db import models

from finalProject.professionals.models import Professional


class Project(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    expenses = models.FloatField()
    description = models.TextField()
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
