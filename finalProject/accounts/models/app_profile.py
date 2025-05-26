from django.contrib.auth import get_user_model
from django.db import models

from finalProject.accounts.validators import validate_phone_number

UserModel = get_user_model()

class Profile(models.Model):
    CHOICES_OCCUPATION = [
        ('Engineer', 'Engineer'),
        ('Architect', 'Architect'),
    ]

    first_name = models.CharField(max_length=30, null=True, blank=True)

    last_name = models.CharField(max_length=30, null=True, blank=True)

    date_of_birth = models.DateField(null=True, blank=True)

    profile_picture = models.ImageField(upload_to='', null=True, blank=True)

    email = models.EmailField(unique=True)

    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])

    occupation = models.CharField(max_length=100, choices=CHOICES_OCCUPATION)

    age = models.IntegerField(
        null=True,
        blank=True,
    )

    about_me = models.TextField(null=True, blank=True)

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name or self.last_name or "Anonymous"