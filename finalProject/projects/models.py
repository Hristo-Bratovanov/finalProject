from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify


UserModel = get_user_model()


class Project(models.Model):
    name = models.CharField(
        max_length=100
    )

    project_photo = models.ImageField(
        upload_to='',
        null=True,
        blank=True
    )

    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    expenses = models.FloatField(
        null=True,
        blank=True
    )

    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True,
        editable=False
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

            super().save(*args, **kwargs)

    def __str__(self):
        return self.name




