from django.db import models
from django.utils import timezone
from markdown import Markdown
from markdown.extensions import codehilite, extra, toc

from pa_user.models import User


# utils
def set_title_img_path(instance, filename):
    return 'title_img/%s/%s' % (instance.author.id, filename)


class Tag(models.Model):
    """文章标签"""
    text = models.CharField(max_length=30)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.text


class Category(models.Model):
    """文章分类"""
    title = models.CharField(max_length=32)
    icon_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.title


class TitleImg(models.Model):
    """标题图"""
    img = models.ImageField(upload_to="title_img/%Y/%m-%d", verbose_name="标题图", blank=True, null=True)


class Article(models.Model):
    """博客文章 model"""
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
    # 分类
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL, related_name='articles')
    # 标签
    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    # 标题图
    title_img = models.ForeignKey(TitleImg, null=True, blank=True, on_delete=models.SET_NULL, related_name='articles')
    # 标题
    title = models.CharField(max_length=100)
    # 正文
    md_cont = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间
    updated = models.DateTimeField(auto_now=True)

    # 评论数量
    @property
    def comment_count(self):
        return self.comments.count()

    # 点赞数量
    @property
    def like_count(self):
        return self.article_like.count()

    def __str__(self):
        return self.title

    def md_change_html(self):
        md = Markdown(extensions=[
            extra.ExtraExtension(),
            codehilite.CodeHiliteExtension(),  # pip install pygments
            toc.TocExtension(),
        ])
        body = md.convert(self.md_cont)
        return md.toc, body  # 渲染后的目录和正文


class AcImg(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_img')
    img = models.ImageField(upload_to='acimg/%Y/%m-%d/', blank=True, null=True)


class UserLike(models.Model):
    """用户点赞文章的记录"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_like')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')  # 用户点赞的文章不能重复
        ordering = ['-created']

    def __str__(self):
        return self.user.username
