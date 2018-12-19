from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class User(AbstractUser):

    REQUIRED_FIELDS = ['email']

    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.username