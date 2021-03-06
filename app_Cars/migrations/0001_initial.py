# Generated by Django 3.1.2 on 2020-10-22 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=256, verbose_name='Производитель')),
                ('modelCar', models.CharField(max_length=128, verbose_name='Модель')),
                ('year_manufacture', models.IntegerField(verbose_name='Год выпуска')),
                ('transmission', models.SmallIntegerField(choices=[(0, ''), (1, 'mechanics'), (2, 'automatic'), (3, 'robot')], default=0, verbose_name='Коробка передачи')),
            ],
        ),
    ]
