from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name