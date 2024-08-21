from rest_framework.permissions import BasePermission

'''
Custom Permission Class 
'''
class ProjectPermission(BasePermission):
   def has_permission(self, request, view):
      if request.method == 'POST':
          return True
      return False