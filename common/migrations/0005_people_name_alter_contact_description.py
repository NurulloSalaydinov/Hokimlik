# Generated by Django 4.2.1 on 2023-05-18 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_contact_alter_pdfnews_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Ismi?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Habar'),
        ),
    ]
