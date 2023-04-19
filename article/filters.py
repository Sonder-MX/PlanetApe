from django_filters import rest_framework as filters

from .models import Article


class ArticleFilter(filters.FilterSet):
    """文章过滤器"""
    title = filters.CharFilter(field_name='title', lookup_expr='icontains', label='文章标题模糊查询')
    category = filters.CharFilter(field_name='category__title', lookup_expr='icontains', label='分类名称模糊查询')
    tag = filters.CharFilter(field_name='tags__text', lookup_expr='icontains', label='标签名称模糊查询')
    created = filters.OrderingFilter(fields=(('latest',)), label='创建时间排序', method='filter_created')

    def filter_created(self, queryset, name, value):
        if value[0] == 'latest':
            return queryset.order_by('-created')
        # 返回空的查询集
        return queryset.none()

    class Meta:
        model = Article
        fields = ['title', 'category', 'tag', 'created']
