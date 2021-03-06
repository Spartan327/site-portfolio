# Generated by Django 3.2 on 2021-05-03 05:31

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vectordrawing',
            name='image',
            field=models.ImageField(storage=pathlib.PurePosixPath('/gallery/media'), upload_to='', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='vectordrawing',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
