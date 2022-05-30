from django.db import models
import datetime


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    date = models.DateTimeField(u'Дата и время', default=datetime.datetime.now())

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Test(models.Model):
    text = models.TextField("Описание")
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сообщение сервера'
        verbose_name_plural = 'Сообщения сервера'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name