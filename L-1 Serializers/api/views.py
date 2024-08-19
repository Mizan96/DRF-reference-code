from django.shortcuts import render

from .models import Student

from .serializers import StudentSerializer

from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse, JsonResponse

# Create your views here.

# Model object - Single Student data
def student_detail(request, pk):
    student = Student.objects.get(id = pk)
    # print(student)
    serializer  = StudentSerializer(student)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)
    
# Queryset - All student data
def student_list(request):
    student = Student.objects.all()
    # print(student)
    serializer  = StudentSerializer(student, many=True)
    # print(serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
    
    
