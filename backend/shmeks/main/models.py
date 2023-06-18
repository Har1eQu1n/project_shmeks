from django.db import models
from .forms import *
from django.urls import reverse_lazy
# Create your models here.
class TicketsShop(models.Model):
    date = models.DateField(verbose_name='Дата концерта')
    city = models.CharField(max_length=256, verbose_name='Город')
    club = models.CharField(max_length=256, verbose_name='Название клуба')
    street = models.CharField(max_length=256, verbose_name='Улица')

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'



class Releases(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='releases', verbose_name='Изображение')
    apple_music = models.URLField(blank=True, null=True)
    spotify = models.URLField(blank=True, null=True)
    vkontakte = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    youtube_music = models.URLField(blank=True, null=True)
    release_description = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Релиз'
        verbose_name_plural = 'Релизы'

class Merch(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название товара')
    image = models.ImageField(verbose_name='Изображение')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    composition = models.TextField(verbose_name='Состав')

    SIZE = (
        (None, 'Выберите размер'),
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL')
    )

    COLOR = (
        (None, 'Выберите цвет'),
        ('wh', 'White'),
        ('bl', 'Black'),
        ('gr', 'Grey'),
        ('vl', 'Violet')
    )

    size = models.CharField(max_length=128, choices=SIZE, verbose_name='Размер', blank=True, null=True)
    color = models.CharField(max_length=128, choices=COLOR, verbose_name='Цвет', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'

































