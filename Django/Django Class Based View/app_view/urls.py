from django.urls import path
from app_view import views

urlpatterns = [
    path('', views.MyView.as_view(name='Mizan'), name='my-view'),
    path('child/', views.MyViewChild.as_view(), name='my-view-child'),
    path('form/', views.contactfun, name='contact-view'),
    path('form2/', views.contact_func_view,{'template_name': 'contact2.html'}, name='contact-view2'),
    path('form3/', views.contact_func_view,{'template_name': 'contact3.html'}, name='contact-view3'),
    path('form-class/', views.ContactClassView.as_view(template_name = 'contact-class.html'), name='contact-class-view'),
    path('form-class2/', views.ContactClassView.as_view(template_name =  'contact-class2.html'), name='contact-class-view2'),
]
