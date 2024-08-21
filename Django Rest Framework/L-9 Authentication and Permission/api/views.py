# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

# CRUD operation
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # only IsStaff=True member can access it
    permission_classes = [IsAdminUser]
    
class StudentViewSet2(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # Overriding Global authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    
class StudentViewSet3(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



