# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tools',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Інструменти',
                'verbose_name': 'Інструмент',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshops',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Ціна')),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 18, 10, 33, 677901, tzinfo=utc), verbose_name='Дата заходу')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 18, 10, 33, 677928, tzinfo=utc), verbose_name='Дата створення')),
                ('address', models.CharField(max_length=100, verbose_name='Адреса')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Опис')),
                ('time', models.PositiveSmallIntegerField(verbose_name='Тривалість')),
                ('visites', models.PositiveIntegerField(default=0, verbose_name='Відвідало')),
                ('age', models.CharField(default='M', choices=[('C', 'Для детей'), ('T', 'Для подростков'), ('M', 'Для молодых'), ('H', 'Для среднего возраста'), ('O', 'Для пожилых')], max_length=1, verbose_name='Вік')),
                ('level', models.CharField(default='L', choices=[('L', 'Начинающий'), ('M', 'опытный'), ('H', 'продвинутый')], max_length=1, verbose_name='Рівень')),
                ('volume', models.PositiveSmallIntegerField(verbose_name='Кількість людей')),
                ('transfer', models.BooleanField(verbose_name='Чи виїздний?')),
                ('buys', models.PositiveIntegerField(default=0, verbose_name='к-ть покупок')),
                ('good', models.ForeignKey(verbose_name='Товар', to='goods.Goods')),
                ('producer', models.ManyToManyField(to='contacts.Contacts', verbose_name='Ведучі')),
                ('tool', models.ManyToManyField(to='workshops.Tools', verbose_name='Інструменти')),
            ],
            options={
                'verbose_name_plural': 'Майстер клас',
                'verbose_name': 'Майстер клас',
            },
            bases=(models.Model,),
        ),
    ]
