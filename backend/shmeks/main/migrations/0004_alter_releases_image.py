# Generated by Django 4.0.4 on 2023-06-17 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_ticketsshop_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='releases',
            name='image',
            field=models.ImageField(upload_to='releases/', verbose_name='Изображение'),
        ),
    ]