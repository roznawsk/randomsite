from django.db import models
from django.forms import ModelForm


class Person(models.Model):
    name = models.CharField(max_length=50)
    nick = models.CharField(max_length=30)
