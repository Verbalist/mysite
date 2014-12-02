# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('description', models.CharField(max_length=1000, verbose_name='Опис товару')),
                ('telephone', models.CharField(max_length=20, blank=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('address', models.CharField(max_length=200, blank=True)),
                ('age', models.CharField(default='M', choices=[('C', 'Для детей'), ('T', 'Для подростков'), ('M', 'Для молодых'), ('H', 'Для среднего возраста'), ('O', 'Для пожилых')], max_length=1, verbose_name='Вік')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Ціна')),
                ('pub_date', models.DateTimeField(verbose_name='Дата заказу')),
                ('base', models.ForeignKey(verbose_name='Основа', to='goods.Bases')),
                ('color', models.ForeignKey(blank=True, verbose_name='Колір', to='goods.Colors')),
                ('style', models.ForeignKey(verbose_name='Стиль', to='goods.Styles')),
                ('technic', models.ForeignKey(verbose_name='Техніка', to='goods.Technics')),
            ],
            options={
                'verbose_name_plural': 'Замовлення',
                'verbose_name': 'Замовлення',
            },
            bases=(models.Model,),
        ),
    ]
