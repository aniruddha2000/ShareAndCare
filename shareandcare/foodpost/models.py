from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class FoodPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=60, default='Excess food')
    description = models.CharField(max_length=200, default='')
    publishing_date = models.DateTimeField(default=timezone.now, blank=True)
    country = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=30, default='')
    address = models.CharField(max_length=300, default='')

    def __str__(self):
        return f"{self.user} - {self.title}"
