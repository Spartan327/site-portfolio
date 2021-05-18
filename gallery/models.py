from django.db import models


class Tag(models.Model):
    title = models.CharField(
        max_length=50, verbose_name='Название', unique=True)

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['title']

    def __str__(self):
        return self.title


class VectorDrawing(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(null=True, verbose_name='Описание')
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    image = models.ImageField(
        verbose_name='Изображение',
        upload_to='gallery/'
    )
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='entries', blank=True)

    class Meta:
        verbose_name_plural = 'Векторные рисунки'
        verbose_name = 'Векторный рисунок'
        ordering = ['-published']

    def __str__(self):
        return self.title
