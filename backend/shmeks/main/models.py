from django.db import models

# Create your models here.
class TicketsShop(models.Model):
    date = models.DateField(verbose_name='Дата концерта')
    city = models.CharField(max_length=256, verbose_name='Город')
    club = models.CharField(max_length=256, verbose_name='Название клуба')
    street = models.CharField(max_length=256, verbose_name='Улица')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'



class Releases(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название')
    image = models.ImageField(upload_to='releases', verbose_name='Изображение')
    list = models.TextField(verbose_name='Ссылки')
    release_description = models.TextField(verbose_name='Описание', blank=True, null=True)

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
        ('s', 'S'),
        ('m', 'M'),
        ('l', 'L'),
        ('xl', 'XL'),
        ('xxl', 'XXL')
    )

    COLOR = (
        ('wh', 'White'),
        ('bl', 'Black'),
        ('gr', 'Grey'),
        ('vl', 'Violet')
    )

    size = models.CharField(max_length=128, choices=SIZE, verbose_name='Размер')
    color = models.CharField(max_length=128, choices=COLOR, verbose_name='Цвет')

    class Meta:
        verbose_name = 'Мерч'
        verbose_name_plural = 'Мерч'































