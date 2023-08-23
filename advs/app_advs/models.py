from django.contrib.auth import get_user_model
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

User = get_user_model()

class Advertisement(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=128)
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='advs/', default='', null=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField(verbose_name='Торг', help_text='Отметье, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')


    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%m:%S')

    @admin.display(description='Дата изменения')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: yellow; font-weight: bold;"> Сегодня в {} </span>', updated_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%m:%S')

    @admin.display(description='Изображение')
    def img_thumbnail(self):
        if self.image:
            return format_html('<img style="height:100px; width:100px;"src={}>', self.image.url)
        else:
            return format_html('<span style="color: red; font-weight: bold;"> Изображение отсутствует </span>')

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

