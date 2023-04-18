"""用户序列化器文件"""
from rest_framework import serializers

from .models import User


class UserDescSerializer(serializers.ModelSerializer):
    """文章列表中引用的嵌套序列化器"""

    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']


class UserRegisterSerializer(serializers.ModelSerializer):
    """用户注册序列化器"""
    password = serializers.CharField(write_only=True, min_length=8, max_length=20, help_text='密码')
    password2 = serializers.CharField(write_only=True, min_length=8, max_length=20, help_text='确认密码')

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')

    def validate(self, attrs):
        """验证两次密码是否一致"""
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError('两次密码不一致')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
