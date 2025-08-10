from django.contrib.auth import get_user_model
from django.db import models

from accounts.validators import validate_phone_number

UserModel = get_user_model()

class CompanyProfile(models.Model):
    CHOICES_INDUSTRY = [
        ('Construction', 'Construction'),
        ('Architecture', 'Architecture'),
        ('Engineering', 'Engineering'),
    ]

    company_name = models.CharField(max_length=100)

    company_logo = models.ImageField(upload_to='')

    industry = models.CharField(max_length=100, choices=CHOICES_INDUSTRY)

    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='company_profile',
    )

    def __str__(self):
        return self.company_name

