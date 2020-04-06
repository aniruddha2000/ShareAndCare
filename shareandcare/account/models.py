from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django_countries.fields import CountryField
from phone_field import PhoneField


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField()
    phone = PhoneField()

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
