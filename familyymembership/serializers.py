from rest_framework import serializers
from .models import Family, FamilyInvite, FamilyMembership
from django.contrib.auth import get_user_model


User = get_user_model()

class FamilyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'name']



class FamilyInviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyInvite
        fields = ['email']


class GetFamilyMemberSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    role = serializers.CharField()
    family_name = serializers.CharField(source='family.name')

    class Meta:
        model = FamilyMembership
        fields = ['username', 'email', 'role', 'family_name', 'joined_at']