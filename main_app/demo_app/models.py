from django.db import models


class Student(models.Model):
    title = models.CharField(max_length=100)
    age = models.IntegerField(default=18)

