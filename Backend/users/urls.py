from django.urls import path
from .views import RegistrationView, LoginView, LogoutView,ChangePasswordView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'users'

urlpatterns = [
    path('accounts/register',RegistrationView.as_view(),name='register'),
    path('accounts/login',LoginView.as_view(),name='register'),
    path('accounts/logout',LogoutView.as_view(),name='register'),
    path('accounts/change-password',ChangePasswordView.as_view(),name='register'),
    path('accounts/token-refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]

