import os

from django.contrib.auth import get_user_model
from django.db import models
from employees.validators import validate_phone_number
from projects.models import Project

UserModel = get_user_model()

class Employee(models.Model):
    CHOICES_JOB_LEVEL = [
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Project Manager', 'Project Manager'),
        ('Team Leader', 'Team Leader'),
    ]

    employee_picture = models.ImageField(upload_to='', null=True, blank=True)

    employee_name = models.CharField(max_length=50)

    years_of_experience = models.IntegerField(null=True, blank=True)

    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])

    email = models.EmailField(max_length=254, null=True, blank=True)

    job_level = models.CharField(max_length=100, choices=CHOICES_JOB_LEVEL)

    about_employee = models.TextField(null=True, blank=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='employees',
    )

    projects = models.ManyToManyField(
        Project,
        related_name='employees',
        blank=True,
    )

    def delete(self, *args, **kwargs):
        if self.employee_picture:
            if os.path.isfile(self.employee_picture.path):
                os.remove(self.employee_picture.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.employee_name
