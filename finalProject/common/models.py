from django.contrib.auth import get_user_model
from django.db import models

from finalProject.projects.models import Project

UserModel = get_user_model()

class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    text = models.TextField(
        max_length=500,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    to_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

class Like(models.Model):
    to_project = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
