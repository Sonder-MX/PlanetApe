from django.contrib import admin

from .models import AcImg, Article, Category, Tag, TitleImg, UserLike

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(AcImg)
admin.site.register(UserLike)
admin.site.register(TitleImg)
