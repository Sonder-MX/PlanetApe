# Generated by Django 4.1.7 on 2023-04-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pa_user', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=120, unique=True, verbose_name='用户名'),
        ),
    ]
