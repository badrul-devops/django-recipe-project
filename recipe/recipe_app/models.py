from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# pylint: disable=no-member


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
