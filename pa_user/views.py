from rest_framework import generics

from .serializers import UserRegisterSerializer


class UserRegisterView(generics.CreateAPIView):
    """用户注册"""
    serializer_class = UserRegisterSerializer
