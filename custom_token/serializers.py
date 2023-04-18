from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenRefreshSerializer)
from rest_framework_simplejwt.state import token_backend


class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        # 获取Token对象
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)

        data['expire'] = refresh.access_token.payload['exp']  # 有效期

        data['username'] = self.user.username
        data['avatar'] = self.user.get_avatar
        data['is_staff'] = self.user.is_staff
        data['is_superuser'] = self.user.is_superuser
        return data

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['avatar'] = user.get_avatar
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        return token


class CustomTokenRefreshSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        # user_uid = decoded_payload['user_id']
        # 获取过期时间
        data['expire'] = decoded_payload['exp']
        return data
