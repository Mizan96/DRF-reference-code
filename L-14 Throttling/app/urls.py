from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views
router = DefaultRouter()

router.register('studentapi', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('list/', views.StudentList.as_view()),
    path('list/', views.StudentCreate.as_view()),
    path('list/<int:pk>/', views.StudentRetrieve.as_view()),
    path('list/<int:pk>/', views.UpdateAPIView.as_view()),
    path('list/<int:pk>/', views.StudentDestroy.as_view()),
]
