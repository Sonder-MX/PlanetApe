from rest_framework import viewsets
from rest_framework_extensions.cache.decorators import cache_response

from .filters import ArticleFilter
from .models import AcImg, Article, Category, Tag, TitleImg, UserLike
from .paginations import ArticlePagination
from .permissions import IsSuperUserOrStuff
from .serializers import (
    AcImgSerializer,
    ArticleDetailSerializer,
    ArticleListSerializer,
    CategoryDetailSerializer,
    CategorySerializer,
    TagSerializer,
    TitleImgSerializer,
    UserLikeSerializer,
)


# redis key 生成器
def custom_key(view_instance, view_method, request, *args, **kwargs):
    page = request.query_params.get("page", 1)  # 获取页码
    # 获取视图集的 redis_key 属性，若不存在，则使用视图集的 class.__name__ 属性
    redis_key = getattr(view_instance, "redis_key", view_instance.__class__.__name__)
    return f"{redis_key}:page{page}"


class AcImgViewSet(viewsets.ModelViewSet):
    queryset = AcImg.objects.all()
    serializer_class = AcImgSerializer
    permission_classes = [IsSuperUserOrStuff]


class TitleImgViewSet(viewsets.ModelViewSet):
    queryset = TitleImg.objects.all()
    serializer_class = TitleImgSerializer
    permission_classes = [IsSuperUserOrStuff]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsSuperUserOrStuff]


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrStuff]

    def get_serializer_class(self):
        if self.action == "list":
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""

    queryset = Article.objects.all().order_by("id")
    serializer_class = ArticleListSerializer
    permission_classes = [IsSuperUserOrStuff]
    pagination_class = ArticlePagination
    filterset_class = ArticleFilter

    redis_key = "article_list"

    def perform_create(self, serializer):  # 重写 perform_create 方法，将作者设置为当前登录用户
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer

    @cache_response(key_func=custom_key)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class UserLikeViewSet(viewsets.ModelViewSet):
    """用户点赞视图集"""

    queryset = UserLike.objects.all()
    serializer_class = UserLikeSerializer
