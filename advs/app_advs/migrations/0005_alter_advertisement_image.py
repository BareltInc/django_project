# Generated by Django 4.2.4 on 2023-08-21 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advs', '0004_advertisement_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default='', upload_to='advs/', verbose_name='Изображение'),
        ),
    ]