from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name