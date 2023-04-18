from rest_framework import viewsets

from .filters import ArticleFilter
from .models import AcImg, Article, Category, Tag, TitleImg
from .paginations import ArticlePagination
from .permissions import IsSuperUserOrStuff
from .serializers import (AcImgSerializer, ArticleDetailSerializer, ArticleListSerializer, CategoryDetailSerializer,
                          CategorySerializer, TagSerializer, TitleImgSerializer)


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
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """博文视图集"""
    queryset = Article.objects.all().order_by('id')
    serializer_class = ArticleListSerializer
    permission_classes = [IsSuperUserOrStuff]
    pagination_class = ArticlePagination
    filterset_class = ArticleFilter

    def perform_create(self, serializer):  # 重写 perform_create 方法，将作者设置为当前登录用户
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        else:
            return ArticleDetailSerializer
