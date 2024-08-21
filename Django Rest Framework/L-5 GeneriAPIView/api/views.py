# GenericAPI View and Model Mixin

from api.models import Student
from api.serializers import StudentSerializer

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin ,UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

# List and Create -  pk not needed
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, rquest, *args, **kwargs):
        return self.list(rquest, *args, **kwargs)
    
    def post(self, rquest, *args, **kwargs):
        return self.create(rquest, *args, **kwargs)


# Retrive, Update, Delete - pk needed
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, rquest, *args, **kwargs):
        return self.retrieve(rquest, *args, **kwargs)
    
    def put(self, rquest, *args, **kwargs):
        return self.update(rquest, *args, **kwargs)
    
    def delete(self, rquest, *args, **kwargs):
        return self.destroy(rquest, *args, **kwargs)