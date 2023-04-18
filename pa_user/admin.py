from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.site_title = '猿星球后台管理'
admin.site.site_header = '猿星球'

# 邮箱：123456@gmail.com
# 密码：sondermx

admin.site.register(User)
