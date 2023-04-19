"""PlanetApe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter  # 路由

from article import views as article_views
from comment import views as comment_views
from custom_token.views import (CustomTokenObtainPairView, CustomTokenRefreshView)
from pa_user.views import UserRegisterView

router = DefaultRouter()
# 文章相关路由
router.register(r'article', article_views.ArticleViewSet, basename='article')
router.register(r'category', article_views.CategoryViewSet, basename='category')
router.register(r'tag', article_views.TagViewSet, basename='tag')
# 评论相关路由
router.register(r'comment', comment_views.CommentViewSet, basename='comment')
# 图片相关路由
router.register(r'titleimg', article_views.TitleImgViewSet, basename='titleimg')
router.register(r'acimg', article_views.AcImgViewSet, basename='acimg')
# 用户相关路由
router.register(r'userlike', article_views.UserLikeViewSet, basename='userlike')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # 可视化接口
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),

    # api
    path('api/user/register/', UserRegisterView.as_view(), name='user_register'),  # 用户注册
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
