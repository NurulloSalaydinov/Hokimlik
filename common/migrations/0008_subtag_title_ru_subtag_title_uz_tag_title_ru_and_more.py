# Generated by Django 4.2.1 on 2023-05-19 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_tag_subtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtag',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='subtag',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Sarlavha'),
        ),
        migrations.AddField(
            model_name='tag',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Sarlavha'),
        ),
    ]
