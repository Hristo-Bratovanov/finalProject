from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

from finalProject.professionals.validators import validate_phone_number

UserModel = get_user_model()


class Professional(models.Model):
    CHOICES_OCCUPATION = [
        ('Engineer', 'Engineer'),
        ('Architect', 'Architect'),
    ]
    name = models.CharField(max_length=100)
    personal_photo = models.URLField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, validators=[validate_phone_number])
    occupation = models.CharField(max_length=100, choices=CHOICES_OCCUPATION)
    age = models.IntegerField()
    number_of_projects = models.IntegerField()
    about_me = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=True, blank=True, editable=False)
    user = models.ForeignKey(to=UserModel, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name




