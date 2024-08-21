from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from api.models import Student
from api.serializers import StudentSerializer


# from django.http import Re
# Create your views here.

# By Default Get method will be called
# @api_view()
# def hello_world(request):
#     return Response({'msg' : 'Hello World'})

# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg' : 'Hello World'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)
#         return Response({'msg' : 'This is post'})
    

# @api_view(['GET','POST'])
# def hello_world(request):
    
#     if request.method == 'GET':
#         return Response({'msg' : 'This is Get Request'})
    
#     if request.method == 'POST':
#         # print(request.data)
#         return Response({'msg' : 'This is Post Request', 'data': request.data})



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request, pk=None):
    
    if request.method == 'GET':
        id = pk
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        student  = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = pk
        student = Student.objects.get(pk=id)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = pk
        student = Student.objects.get(pk=id)
        student.delete()
        return Response({'msg': 'Data Deleted'})