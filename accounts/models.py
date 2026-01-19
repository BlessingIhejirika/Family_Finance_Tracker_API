from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)

    profile_picture = models.ImageField( upload_to='profiles/', blank=True, null=True)

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('member', 'Member'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

   
    def __str__(self):
        return self.username
