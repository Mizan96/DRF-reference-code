# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from api.token_generator import CustomAuthToken
from rest_framework.authentication import TokenAuthentication
from api.custom_auth import CustomAuthentication



# CRUD operation
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    # authentication_classes = [CustomAuthToken]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]
  
    
    




