from django.db import models
from django.contrib.auth.models import  User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, help_text='Required.')
    phonenumber = models.CharField(max_length=10, help_text='Required.')
    age = models.CharField(max_length=2, help_text='Required.')

    def __str__(self):
        return self.user.username



