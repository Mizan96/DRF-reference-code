from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from user_api.serializers import UserSerializer, UserSerializerWithToken


from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class SignupAPI(CreateAPIView):
    """
    User registration api view
    api end pint: http://127.0.0.1:8000/api/signup/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializerWithToken

@api_view(['POST'])
def user_registration(request):
    data = request.data
    try:
        user = User.objects.create(
                username=data['username'],
                password=make_password(data['password']),
                is_active=False
            )
        print(user)
        serializer = UserSerializerWithToken(user, many=False)
        print(serializer.data['token'])
        return Response(serializer.data['token']) 
    except:
        return Response('User with is username is already exist')
    

"""
User Signin 
api end point: http://127.0.0.1:8000/api/token/
"""
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_detail(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_update(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_delete(request):
    user = request.user
    user.delete()
    return Response('Data is deleted successfully')


class UserApprovalAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]



