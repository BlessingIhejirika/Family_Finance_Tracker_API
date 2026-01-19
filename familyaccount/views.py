from django.shortcuts import render
import random
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from familyymembership.models import FamilyMembership
from .models import FamilyAccount
from .serializers import FamilyAccountSerializer



class CreateFamilyAccountView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        membership = FamilyMembership.objects.filter(
            user=request.user
        ).first()

        if not membership:
            return Response(
                {"detail": "You are not a member of any family"},
                status=status.HTTP_403_FORBIDDEN
            )

        family = membership.family

        if hasattr(family, 'account'):
            return Response(
                {"detail": "Family account already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        account_number = f"FA-{random.randint(100000, 999999)}"

        account = FamilyAccount.objects.create(
            family=family,
            account_name=family.name,
            account_number=account_number,
            created_by=request.user
        )

        # OPTIONAL: auto-promote creator to admin
        if membership.role != 'admin':
            membership.role = 'admin'
            membership.save()

        serializer = FamilyAccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
