# Generated by Django 4.2.1 on 2023-05-08 17:56

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('slug', models.SlugField(verbose_name='*')),
            ],
            options={
                'verbose_name': 'Turkum',
                'verbose_name_plural': 'Turkumlar',
            },
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('slug', models.SlugField(verbose_name='*')),
                ('image', models.ImageField(blank=True, null=True, upload_to='detail_images/%y/%m/%d/', verbose_name='Rasm')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Kontent')),
                ('content_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Kontent')),
                ('content_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Kontent')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Korilganlar soni')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Malumot',
                'verbose_name_plural': 'Malumotlar',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Yangilik uchun sarlavha')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Yangilik uchun sarlavha')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Yangilik uchun sarlavha')),
                ('slug', models.SlugField(verbose_name='*')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Kontent')),
                ('content_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Kontent')),
                ('content_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Kontent')),
                ('views_count', models.PositiveIntegerField(default=0, verbose_name='Korilganlar soni')),
                ('is_uzbek', models.BooleanField(default=True, verbose_name='Ozbekiston yangiligimi?')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Yangilik',
                'verbose_name_plural': 'Yangiliklar',
            },
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='government/%y/%m/%d/', verbose_name='Rasm')),
                ('who', models.CharField(max_length=255, verbose_name='Kimligi?')),
                ('who_uz', models.CharField(max_length=255, null=True, verbose_name='Kimligi?')),
                ('who_ru', models.CharField(max_length=255, null=True, verbose_name='Kimligi?')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Malumot')),
                ('content_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Malumot')),
                ('content_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Malumot')),
                ('is_governor', models.BooleanField(default=True, verbose_name='Rahbar?')),
            ],
            options={
                'verbose_name': 'Rahbariyat',
                'verbose_name_plural': 'Rahbariyatlar',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Sarlavha')),
                ('slug', models.SlugField(verbose_name='*')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.category', verbose_name='Turkum')),
            ],
            options={
                'verbose_name': 'Qoshimcha turkum',
                'verbose_name_plural': 'Qoshimcha turkumlar',
            },
        ),
        migrations.CreateModel(
            name='Pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='PDF uchun sarlavha')),
                ('pdf_file', models.FileField(upload_to='pdf/%y/%m/%d/', verbose_name='Fayl')),
                ('detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.detail', verbose_name='Qaysi malumot uchun?')),
            ],
            options={
                'verbose_name': 'PDF Fayl',
                'verbose_name_plural': 'PDF Fayllar',
            },
        ),
        migrations.AddField(
            model_name='detail',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.subcategory', verbose_name='Qoshimcha turkum'),
        ),
    ]
