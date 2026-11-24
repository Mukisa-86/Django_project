from django.db import models
from django.utils import timezone
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - UGX {self.price}"


class Product(models.Model):
    name = models.CharField(max_length=300, default="")
    category = models.CharField(max_length=100, default="")
    price = models.FloatField(default=0.0)
    expiry = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.price}"
