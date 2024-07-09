from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
