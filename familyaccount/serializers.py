
from rest_framework import serializers
from .models import FamilyAccount

class FamilyAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyAccount
        fields = [
            'id',
            'account_name',
            'account_number',
            'created_at',
            'is_active'
        ]
        read_only_fields = ['account_number', 'created_at', 'is_active']