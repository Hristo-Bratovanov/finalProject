import os

from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

UserModel = get_user_model()

class Project(models.Model):
    name = models.CharField(
        max_length=100
    )

    project_photo = models.ImageField(
        upload_to='projects/',
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
        on_delete=models.CASCADE,
        related_name='projects',
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

            Project.objects.filter(pk=self.pk).update(slug=self.slug)

    def delete(self, *args, **kwargs):
        if self.project_photo:
            if os.path.isfile(self.project_photo.path):
                os.remove(self.project_photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name




