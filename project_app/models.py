from django.db import models
from accounts.models import User


class Family(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_families')
    members = models.ManyToManyField(User, related_name='families')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
