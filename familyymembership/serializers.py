from rest_framework import serializers
from .models import Family, FamilyInvite

class FamilyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name']



class FamilyInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInvite
        fields = ['email']
