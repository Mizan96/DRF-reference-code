from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from api.models import User
# Register your models here

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'email')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(User, CustomUserAdmin)

