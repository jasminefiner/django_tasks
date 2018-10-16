from django.conf import settings
from django.db import models

# Create your models here.


class Task(models.Model):
    body = models.CharField(max_length=30)
    due = models.DateField()
    author = models.ForeignKey(
                settings.AUTH_USER_MODEL,
                on_delete=models.CASCADE,
                null=True
                )
