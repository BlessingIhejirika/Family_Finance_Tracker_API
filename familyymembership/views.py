from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Family, FamilyMembership, FamilyInvite
from .serializers import FamilyCreateSerializer, FamilyInviteSerializer, GetFamilyMemberSerializer
from django.shortcuts import get_object_or_404


class CreateFamilyAdmin(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FamilyCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        family= serializer.save()

        FamilyMembership.objects.create(
            user=request.user,
            family=family,
            role='admin'
        )

        return Response(
            {
                "message": "Family admin created successfully",
                "familyadmin": serializer.data
            },
            status=status.HTTP_201_CREATED
        )



class InviteFamilyMember(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        membership = FamilyMembership.objects.filter(
            user=request.user,
            role='admin'
        ).first()

        if not membership:
            return Response(
                {"detail": "Only admins can invite"},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = FamilyInviteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        invite = FamilyInvite.objects.create(
            family=membership.family,
            email=serializer.validated_data['email']
        )

        return Response({
            "invite_token": str(invite.token)
        })



class AcceptInvite(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('invite_token')
        if not token:
            return Response({"detail": "Invite token required"}, status=400)

        invite = get_object_or_404(
            FamilyInvite,
            token=token,
            is_used=False
        )

        FamilyMembership.objects.create(
            user=request.user,
            family=invite.family,
            role='member'
        )

        invite.is_used = True
        invite.save()

        return Response({"message": "Joined family successfully"})


class GetAFamilyMembers(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, family_id):
        family = get_object_or_404(Family, id=family_id)
      
        if not FamilyMembership.objects.filter(user=request.user, family=family).exists():
            return Response({"detail": "You are not a member of this family"}, status=403)

        memberships = FamilyMembership.objects.filter(family=family)
        serializer = GetFamilyMemberSerializer(memberships, many=True)
        return Response(serializer.data)
