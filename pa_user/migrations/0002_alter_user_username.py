# Generated by Django 4.1.7 on 2023-04-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pa_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=120, verbose_name='用户名'),
        ),
    ]
