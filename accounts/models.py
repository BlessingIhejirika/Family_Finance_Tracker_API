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

    # def is_18_or_older(self):
    #     if not self.date_of_birth:
    #         return False
    #     today = date.today()
    #     age = today.year - self.date_of_birth.year - (
    #         (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
    #     )
    #     return age >= 18

    def __str__(self):
        return self.username
