from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token

from api.token_generator import CustomAuthToken
from api import views
router = DefaultRouter()

router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('gettoken/', obtain_auth_token),
    # path('gettoken/', CustomAuthToken.as_view()),
]

'''
http POST http://127.0.0.1:8000/gettoken/ username="user1" password="Test@1996"
format for sendind http request and generating web token
for that you need to install: "pip install httpie"

another way og generating token:
    python manage.py drf_create_token userName
'''

'''
httpie:
http http://127.0.0.1:8000/studentapi/ -->get request without authentication

http http://127.0.0.1:8000/studentapi/ 'Authorization:Token d865391fb2d9a3bd9f5c91f4c0ba0311af59c093' --> get with token authentication

http -f POST http://127.0.0.1:8000/studentapi/ name=Mizan roll=101 city=Belkuchi 
'Authorization:Token d865391fb2d9a3bd9f5c91f4c0ba0311af59c093' --> post data with token authentication

http PUT http://127.0.0.1:8000/studentapi/13/ name=Mizan roll=101 city=Sirajganj 
'Authorization:Token d865391fb2d9a3bd9f5c91f4c0ba0311af59c093' --> put with token authentication

http DELETE http://127.0.0.1:8000/studentapi/13/ 
'Authorization:Token d865391fb2d9a3bd9f5c91f4c0ba0311af59c093' --> delete with token authentication

'''