from django import forms
from django.forms import ModelForm
from tasks.models import Task


class NewTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['body', 'due']

