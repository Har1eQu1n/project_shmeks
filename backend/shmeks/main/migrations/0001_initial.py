# Generated by Django 4.0.4 on 2023-06-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название товара')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('composition', models.TextField(verbose_name='Состав')),
                ('size', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('xxl', 'XXL')], max_length=128, verbose_name='Размер')),
                ('color', models.CharField(choices=[('wh', 'White'), ('bl', 'Black'), ('gr', 'Grey'), ('vl', 'Violet')], max_length=128, verbose_name='Цвет')),
            ],
        ),
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('list', models.TextField(verbose_name='Ссылки')),
                ('release_description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='TicketsShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата создания')),
                ('city', models.CharField(max_length=256, verbose_name='Город')),
                ('club', models.CharField(max_length=256, verbose_name='Название клуба')),
                ('street', models.CharField(max_length=256, verbose_name='Улица')),
            ],
        ),
    ]