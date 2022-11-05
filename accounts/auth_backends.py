from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User


class UserEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        kwargs = {'email': username} if '@' in username else {'username': username}
        try:
            user = User.objects.get(**kwargs)
            return user if user.check_password(password) else None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
