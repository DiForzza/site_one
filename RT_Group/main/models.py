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