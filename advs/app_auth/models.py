from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(verbose_name='Имя пользователя', max_length=30)
    name = models.CharField(verbose_name='Имя пользователя', max_length=30)
    surname = models.CharField(verbose_name='Имя пользователя', max_length=30)
    password = models.TextField(verbose_name='Пароль', max_length=30)
    password_confirm = models.CharField(verbose_name='Имя пользователя', max_length=30)