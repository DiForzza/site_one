# Generated by Django 4.0.3 on 2022-05-12 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_test_options_alter_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 12, 12, 36, 44, 588501), verbose_name='Дата и время'),
        ),
    ]