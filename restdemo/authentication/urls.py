from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationView

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]