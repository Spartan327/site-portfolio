# Generated by Django 3.2 on 2021-05-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_alter_vectordrawing_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vectordrawing',
            name='image',
            field=models.ImageField(upload_to='gallery/', verbose_name='Изображение'),
        ),
    ]
