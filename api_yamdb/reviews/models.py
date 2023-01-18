from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Название')
    slug = models.SlugField(max_length=50,
                            verbose_name='Указатель',
                            unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
