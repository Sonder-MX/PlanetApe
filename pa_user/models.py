from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            username = email.split('@')[0]

        # 去掉password2
        extra_fields.pop('password2', None)

        # normalize_email将email转换为小写，避免重复的email
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='邮箱地址',
        max_length=50,
        unique=True,
    )
    username = models.CharField(verbose_name='用户名', max_length=120, unique=True)
    date_joined = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    avatar = models.ImageField(verbose_name='用户头像', upload_to='avatar/%Y/%m', default='avatar/default.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # 用于登录的字段
    REQUIRED_FIELDS = ['username']  # 创建用户时必须填写的字段

    def __str__(self):
        return self.email

    @property
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return ''

    class Meta:
        db_table = 'pa_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
