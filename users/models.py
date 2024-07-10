from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True, verbose_name="Активность сотрудника")
    token = models.CharField(max_length=50, verbose_name='токен')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
