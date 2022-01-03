from django.db import models

# Create your models here.
class ToDo(models.Model):
    added_date = models.TimeField()
    text = models.CharField(max_length=200)
