from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from .views import (
    LoginView,
    LogoutView,
    RegistrationView,
    FirstStepRegistrationView,
    SecondStepRegistrationView,
)

app_name = "auth_app"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path(
        "registration/first-step/",
        FirstStepRegistrationView.as_view(),
        name="first-step-registration",
    ),
    path(
        "registration/second-step/",
        SecondStepRegistrationView.as_view(),
        name="second-step-registration",
    ),
]
