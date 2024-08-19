from api.serializers import StudentSerializer
from api.models import Student

from rest_framework.generics import ListAPIView

from api.pagination import PageNumberPagination, PageLimitOffsetPagination,MyCursorPagination

# Create your views here.
class StudentList(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = PageLimitOffsetPagination
    pagination_class = MyCursorPagination
    
    



