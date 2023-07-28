from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    time_required = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)