# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import (IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions,
                                        DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions)

'''
I have to check DjangoObjectPermissions by myself
'''


# CRUD operation
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    # parser_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # only IsStaff=True member can access it
    # permission_classes = [IsAdminUser]
    
    '''
    Only Authenticated user can see list or detail view 
    Users have to assign model permission to Create, Update and delete
    '''
    # permission_classes = [DjangoModelPermissions]
    
    '''
    Authenticated user only have read only permission 
    Users have to assign model permission to Create, Update and delete
    '''
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    
    




