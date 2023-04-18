from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomTokenRefreshSerializer, CustomTokenSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer


class CustomTokenRefreshView(TokenObtainPairView):
    serializer_class = CustomTokenRefreshSerializer
