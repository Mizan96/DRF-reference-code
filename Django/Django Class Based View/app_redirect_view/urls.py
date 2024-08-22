from django.urls import path
from app_redirect_view import views
urlpatterns = [
    path('', views.TemplateView.as_view(template_name='redirect/index.html'), name='home-page'),
    path('home/', views.RedirectView.as_view(url=('/')), name='home'),
    path('index/', views.RedirectView.as_view(url=('/')), name='index'),
    path('home2/', views.RedirectView.as_view(pattern_name='home-page'), name="home2"),
    path('news/', views.NewSite.as_view(), name='news'),
    # path('news/<int:pk>/', views.NewSite2.as_view(), name='news2'),
    # path('<int:pk>/', views.TemplateView.as_view(template_name='redirect/index.html'), name='home3'),
    path('news/<slug:post>/', views.NewSite2.as_view(), name='news2'),
    path('<slug:post>/', views.TemplateView.as_view(template_name='redirect/index.html'), name='home3'),
]
