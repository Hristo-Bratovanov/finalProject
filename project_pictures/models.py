import os

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from projects.models import Project

UserModel = get_user_model()

class ProjectPicture(models.Model):
    picture = models.ImageField(
        upload_to='projects_photos/'
    )

    description = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(10)],
        null=True,
        blank=True
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='pictures',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def delete(self, *args, **kwargs):
        # This will correctly delete the file from Azure Blob Storage
        self.picture.delete(save=False)
        # Now, call the parent method to delete the database record
        super().delete(*args, **kwargs)