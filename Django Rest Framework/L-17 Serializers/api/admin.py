from django.contrib import admin

from api.models import Singer, Song, Student

# Register your models here.
@admin.register(Singer)
class SingerSdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']
    ordering = ['id']
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer', 'duration']
    ordering = ['id']
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']
    ordering = ['id']