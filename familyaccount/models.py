from django.db import models
from familyymembership.models import Family
from django.conf import settings

User = settings.AUTH_USER_MODEL

class FamilyAccount(models.Model):
    family = models.OneToOneField(Family, on_delete=models.CASCADE, related_name='account')
    account_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, unique=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_name} ({self.account_number})"
