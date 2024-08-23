from django.urls import path, include
from user_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserApprovalAPI, basename='approval')

urlpatterns = [
    path('user/registration/', views.user_registration, name='user-signup'),
    path('user/profile/', views.user_detail, name='user-profile'),
    path('user/update/', views.user_update, name='user-update'),
    path('user/delete/', views.user_delete, name='user-delete'),
    path('user/', include(router.urls)),
]


