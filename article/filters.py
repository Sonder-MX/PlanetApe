from django_filters import rest_framework as filters

from .models import Article


class ArticleFilter(filters.FilterSet):
    """文章过滤器"""
    title = filters.CharFilter(field_name='title', lookup_expr='icontains', label='文章标题模糊查询')
    category = filters.CharFilter(field_name='category__title', lookup_expr='icontains', label='分类名称模糊查询')
    tag = filters.CharFilter(field_name='tags__text', lookup_expr='icontains', label='标签名称模糊查询')
    sort = filters.OrderingFilter(fields=(('comment_count', 'comment_count')), label='排序')

    class Meta:
        model = Article
        fields = ['title', 'category', 'tag', 'sort']
