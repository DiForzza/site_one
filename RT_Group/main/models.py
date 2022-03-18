from django.db import models


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class UserLoginForm(models.Model):
    email = models.EmailField(max_length = 100)
    password = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.email