from django.urls import path
from .views import RegistrationView, TokenObtain, TokenRefresh, ActivateAccount

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('token/', TokenObtain.as_view()),
    path('token/refresh', TokenRefresh.as_view()),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view())
]