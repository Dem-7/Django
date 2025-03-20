from django.db import models

# Create your models here.
class Novost(models.Model):
    a = models.CharField('Название новости' , max_length=70)
    b = models.CharField('Описание новости' ,max_length=70)
    c = models.TextField('Новость')
    d = models.DateTimeField('Дата публикации')
    e = models.CharField('Автор', max_length=30)

    def __str__(self):
        return self.a

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'