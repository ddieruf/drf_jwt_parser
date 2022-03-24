from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .permissions import IsActive
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from .tokens import account_activation_token

class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TokenObtain(TokenObtainPairView):
    permission_classes = [IsActive,]

class TokenRefresh(TokenRefreshView):
    permission_classes = [IsActive,]

class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token) and user.is_active == False:
            user.is_active = True
            user.save()

            return Response('Account activated!')
        else:
            return Response('Invalid link or token expired!')