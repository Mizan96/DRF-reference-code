from django.urls import path

from app_crud import views

urlpatterns = [
    path('', views.UserView.as_view(), name='home-student'),
    path('<int:pk>/', views.UserUpdateView.as_view(), name='update-student'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete-student'),
]
