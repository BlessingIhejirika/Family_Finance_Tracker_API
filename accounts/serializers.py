from rest_framework.authtoken.models import Token
from datetime import date
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_picture', 'date_of_birth', 'role',]
        read_only_fields = ['date_of_birth','role',]



from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from datetime import date

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default='member') 

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'date_of_birth',
            'role', 
        ]

    def validate_date_of_birth(self, value):
        """
        Ensure user is at least 18 years old
        """
        today = date.today()
        age = today.year - value.year - (
            (today.month, today.day) < (value.month, value.day)
        )
        if age < 18:
            raise serializers.ValidationError(
                "You must be at least 18 years old to register."
            )
        return value

    def create(self, validated_data):
       
        role = validated_data.pop('role', 'member')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            date_of_birth=validated_data['date_of_birth'],
            role=role,  
        )

        token =Token.objects.create(user=user)
        user.token = token.key
        return user



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'],
            password=attrs['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid username or password")

        attrs['user'] = user
        return attrs