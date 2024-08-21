from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework.routers import DefaultRouter

from rest_framework.authtoken.views import obtain_auth_token
from api import views
router = DefaultRouter()



router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token-refresh-view'),
    path('verifytoken/', TokenVerifyView.as_view(), name='verify-token'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]


'''
http POST http://127.0.0.1:8000/gettoken/ username="user1" password="Test@1996"
format for sending http request and generating Simple JWT
'''

'''
httpie:

http -f POST http://127.0.0.1:8000/gettoken/ username='user1' password='Test@1996' --> get token


http POST http://127.0.0.1:8000/verifytoken/ token="...." --> Verify Token

http POST http://127.0.0.1:8000/refreshtoken/ refresh="" --> get new access token using refresh token

'''