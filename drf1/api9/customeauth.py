from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomeAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        password = request.GET.get('password')
        print(username, password)
        if username and password:
            try:
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return (user, None)
            except User.DoesNotExist:
                pass
        raise AuthenticationFailed