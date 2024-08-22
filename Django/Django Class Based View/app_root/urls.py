from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('views/', include('app_view.urls')),
    # path('templates/', include('app_template_view.urls')),
    # path('', include('app_redirect_view.urls')),
    path('', include('app_crud.urls')),
]
