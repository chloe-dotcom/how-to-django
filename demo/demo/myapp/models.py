from django.db import models

# Create your models here.


# ORM: object relational mapping
# - write python code to write database models
# - connects OOP to databases by converting data automatically

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    difficulty = models.IntegerField(default=None, null=True)