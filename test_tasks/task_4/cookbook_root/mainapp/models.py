from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Наименование категории', max_length=128, unique=True)
    description = models.TextField(verbose_name='Описание категории', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Ingredient(models.Model):
    name = models.CharField(verbose_name='Наименование продукта', max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название блюда', max_length=128)
    image = models.ImageField(upload_to='dishes_images', blank=False)
    short_desc = models.CharField(verbose_name='Краткое описание', max_length=64, blank=True)
    description = models.TextField(verbose_name='Содержание рецепта', blank=False)
    time_create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время изменения', auto_now=True)
    is_active = models.BooleanField(verbose_name='Активен', default=True)
    author = models.CharField(verbose_name='Автор', max_length=64, default='автор не известен')
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        return f'{self.name} ({self.category})'

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
