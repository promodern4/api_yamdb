from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import validate_year


class UserRole(models.TextChoices):
    ADMIN = 'admin', 'Администратор'
    MODERATOR = 'moderator', 'Модератор'
    USER = 'user', 'Пользователь'


class User(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='Электронная почта',
        unique=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=True,
        unique=True,
    )
    role = models.CharField(
        max_length=50,
        choices=UserRole.choices,
        default=UserRole.USER,
        verbose_name='Роль'
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True,
    )

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact='me'),
                name='username_is_not_me'
            ),
            models.UniqueConstraint(
                fields=['username', 'email'], name='unique_user'
            )
        ]


class Category(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=256)
    slug = models.SlugField(verbose_name='Указатель',
                            max_length=50,
                            unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

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
        ordering = ['name']

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(verbose_name='Название',
                            max_length=200)
    year = models.PositiveIntegerField(verbose_name='Дата выхода',
                                       validators=[validate_year,
                                                   MinValueValidator(1900)])
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
        ordering = ['name']

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


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='Автор'
    )
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews',
        verbose_name='Произведение'
    )
    score = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(10)],
        verbose_name='Оценка'
    )
    text = models.TextField(verbose_name='Текст отзыва')
    pub_date = models.DateTimeField(
        auto_now_add=True, db_index=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_author_title'
            )
        ]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор'
    )
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Отзыв'
    )
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['pub_date']