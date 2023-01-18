from django.db import models

from .validators import validate_year


class Category(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=256)
    slug = models.SlugField(verbose_name='Указатель',
                            max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


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


class Title(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=200)
    year = models.IntegerField(verbose_name='Дата выхода',
                               validators=[validate_year])
    rating = models.IntegerField(verbose_name='Рейтинг',
                                 null=True,
                                 default=None)
    description = models.TextField(verbose_name='Описание',
                                   null=True,
                                   blank=True)
    genre = models.ManyToManyField(Genre,
                                   verbose_name='Жанр',
                                   through='GenreTitle')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 null=True)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE)
    genre = models.ForeignKey(
        Genre,
        verbose_name='Жанр',
        on_delete=models.CASCADE)
