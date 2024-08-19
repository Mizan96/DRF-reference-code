from django.shortcuts import render

from api.serializers import StudentSerializer
from api.models import Student

from rest_framework.generics import ListAPIView
'''
django-filter local settings
'''
from django_filters.rest_framework import DjangoFilterBackend

'''
For search functionality
'''
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # Both search and filter is added
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # OrderingFilter will by default add all the fields for filtering
    ordering_fields = ['name', 'city']
    '''
    http://127.0.0.1:8000/studentapi/?city=Dhaka -->use this pattern to search
    http://127.0.0.1:8000/studentapi/?city=Sirajganj&name=Mizan --> two fields search
    '''
    filterset_fields = ['city', 'name']
    # search_fields = ['city', 'name']
    # search_fields = ['=name']
    # search_fields = ['^name']
    search_fields = ['=name']
    '''
    '^fieldName' --> Search with starting letter
    '=fieldName' --> Exact search
    '''
    
    '''
    # filtering data using logged in user 
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
    '''


