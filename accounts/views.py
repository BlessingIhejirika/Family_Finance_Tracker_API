from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.permissions import AllowAny



CustomUser = get_user_model() 

class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer           

class UserLoginView(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                "token": token.key,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                }
            },
            status=status.HTTP_200_OK
        )