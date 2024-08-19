# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication



# CRUD operation
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

'''
#### Using httpie: ####
http http://127.0.0.1:8000/studentapi/ 
'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNj' --> get data using Simple JWT Authentication

http -f POST http://127.0.0.1:8000/studentapi/ name=Mizan roll=101 city=Belkuchi 
'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNj' --> Posting Data usinf Simple JWT Authentication

http PUT http://127.0.0.1:8000/studentapi/13/ name=Mizan roll=101 city=Belkuchi 
'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNj' -->Update using Simple JWT

http DELETE http://127.0.0.1:8000/studentapi/13/
'Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNj' -->Delete using Simple JWT
'''
  
    
    




