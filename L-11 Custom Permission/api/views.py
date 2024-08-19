# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from api.custompermissions import ProjectPermission




# CRUD operation
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [ProjectPermission]

    
    




