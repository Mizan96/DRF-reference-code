from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer

from rest_framework.renderers import JSONRenderer

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        # print(json_data) 
        # b'{"name": "Sourov", "roll": 1, "city": "Sirajganj"}'
        stream  = io.BytesIO(json_data)
        # print(stream)
        # <_io.BytesIO object at 0x000001A47B450B30>
        python_data = JSONParser().parse(stream)
        # print(python_data)
        # {'name': 'Sourov', 'roll': 1, 'city': 'Sirajganj'}
        serializer = StudentSerializer(data = python_data)
        # print(serializer)
        # StudentSerializer(data={'name': 'Sourov', 'roll': 1, 'city': 'Sirajganj'}):
        # name = CharField(max_length=100)
        # roll = IntegerField()
        # city = CharField(max_length=100)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data created'}
            json_data = JSONRenderer().render(res)
            # print(json_data)
            # b'{"msg":"Data created"}'
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')
        
