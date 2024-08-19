from rest_framework.authentication import BaseAuthentication

from django.contrib.auth.models import User

from rest_framework.exceptions import AuthenticationFailed

'''
Url will be something like this
http://127.0.0.1:8000/studentapi/?username=user1
'''

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed('No such User')
        return (user, None)