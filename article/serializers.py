from rest_framework import serializers

from comment.serializers import CommentSerializer
from pa_user.serializers import UserDescSerializer

from .models import AcImg, Article, Category, Tag, TitleImg


class TitleImgSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='titleimg-detail')

    class Meta:
        model = TitleImg
        fields = '__all__'


class TagSerializer(serializers.HyperlinkedModelSerializer):

    @staticmethod
    def check_tag_obj_exists(validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError(f'Tag with text {text} exists.')

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class AcImgSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='acimg-detail')

    class Meta:
        model = AcImg
        fields = '__all__'


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    """
    文章序列化器父类
    """
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)
    # category 的嵌套序列化字段
    category = CategorySerializer(read_only=True)
    # tag 字段
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(), many=True, required=False, slug_field='text')

    #  覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')
        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)
        return super().to_internal_value(data)

    title_img = TitleImgSerializer(read_only=True)
    title_img_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    @staticmethod
    def validate_title_img_id(value):
        if not TitleImg.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError(f"TitleImg with id {value} not exists.")
        return value

    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id 字段的验证器 400 error
    @staticmethod
    def validate_category_id(value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError(f"Category with id {value} not exists.")
        return value


class ArticleListSerializer(ArticleBaseSerializer):
    """文章列表序列化器"""

    # 部分内容
    part_cont = serializers.SerializerMethodField()

    def get_part_cont(self, obj):
        res = obj.md_cont[:120]
        res = res.replace('\r', '').replace('\n', '').replace('#', '').replace('`', '').replace(' ', '')
        return res + "......"

    # 点赞的数量
    lkct = serializers.SerializerMethodField()

    def get_lkct(self, obj):
        return obj.like_count

    cmtt = serializers.SerializerMethodField()

    def get_cmtt(self, obj):
        return obj.comment_count

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'md_cont': {'write_only': True}, 'created': {'read_only': True}, 'tags': {'read_only': True}}


class ArticleDetailSerializer(ArticleBaseSerializer):
    id = serializers.IntegerField(read_only=True)
    body_html = serializers.SerializerMethodField()
    toc_html = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    def get_toc_html(self, obj):
        return obj.md_change_html()[0]

    def get_body_html(self, obj):
        return obj.md_change_html()[1]

    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'md_cont': {'write_only': True}, 'created': {'read_only': True}, 'tags': {'read_only': True}}
