from django.db import models

# Create your models here.


class Task(models.Model):
    body = models.CharField(max_length=30)
    due = models.DateField()
