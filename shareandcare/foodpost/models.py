from django.db import models
from django.contrib.auth.models import User

class FoodPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=60, default='Excess food')
    description = models.CharField(max_length=200, default='')
    country = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=30, default='')
    location_link = models.URLField(default='')

    def __str__(self):
        return f"{self.user} - {self.title}"
