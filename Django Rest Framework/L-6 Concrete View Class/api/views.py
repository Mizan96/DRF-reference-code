# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class LCStudentAPI(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class RUDStudentAPI(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


