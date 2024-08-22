from django.urls import path
from app_template_view import views

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='templates_view/index.html'), name='template-view'),
     path('home/<int:class>/<str:session>/<str:district>/', views.HomePage.as_view(extra_context = {'course':'python'} ), name='template-home-view'),
]