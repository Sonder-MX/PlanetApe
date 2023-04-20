# Generated by Django 4.1.7 on 2023-04-20 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_titleimg_alter_article_title_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlike',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_like', to='article.article'),
        ),
        migrations.AlterField(
            model_name='userlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
    ]