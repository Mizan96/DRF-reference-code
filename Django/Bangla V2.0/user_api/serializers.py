'''
Signup -->ok
Signin -->ok
Forget password
Reset password
Profile -->ok
Profile update -->ok
Approval API (for approving newly registered user) -->ok
'''
from rest_framework import serializers
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Customizing Simple JWT 
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(token)
        # Add custom claims
        token['name'] = user.username
        # ...

        return token

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user update, delete and retrieve
    """
    class Meta:
        model = User
        fields = ['id','username']

class UserSerializerWithToken(UserSerializer):
    """
    Django's default User Model serializer class 
    """
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, user):
        """
        Creating Simple JWT manually
        """
        token_obj = MyTokenObtainPairSerializer()
        token = token_obj.get_token(user)
         
        return {
        'refresh': str(token),
        'access': str(token.access_token),
        }
    
    class Meta:
        model = User
        fields = ['username', 'password','token','is_active']
        extra_kwargs = {'password': {'write_only': True}}

