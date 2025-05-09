from django.db import models

from finalProject.professionals.validators import validate_phone_number


class Professional(models.Model):
    CHOICES_OCCUPATION = [
        ('Engineer', 'Engineer'),
        ('Architect', 'Architect'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])
    occupation = models.CharField(max_length=100, choices=CHOICES_OCCUPATION)
    age = models.IntegerField()
    number_of_projects = models.IntegerField()
    about_me = models.TextField(blank=True, null=True)




