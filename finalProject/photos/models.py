from django.contrib.auth import get_user_model
from django.db import models
from finalProject.projects.models import Project

UserModel = get_user_model()

class Photo(models.Model):
    photo = models.ImageField(
        upload_to='mediafiles/'
    )

    description = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )

    tagged_projects = models.ManyToManyField(
        Project,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )