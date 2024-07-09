from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from rest_framework.permissions import AllowAny

from users.views import UserListView, UserRetrieveView, UserCreateView, UserUpdateView, UserDestroyView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),

    path('', UserListView.as_view()),
    path('detail/<int:pk>/', UserRetrieveView.as_view()),
    path('create/', UserCreateView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('delete/<int:pk>/', UserDestroyView.as_view()),
]
