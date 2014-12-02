# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bases',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('size', models.CharField(max_length=50, help_text='Якщо декілька то через Х, вводити у см', verbose_name='Розмір')),
            ],
            options={
                'verbose_name_plural': 'Основи',
                'verbose_name': 'Основа',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Кольори',
                'verbose_name': 'Колір',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('price', models.PositiveSmallIntegerField(verbose_name='Ціна')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Опис')),
                ('age', models.CharField(default='M', choices=[('C', 'Для детей'), ('T', 'Для подростков'), ('M', 'Для молодых'), ('H', 'Для среднего возраста'), ('O', 'Для пожилых')], max_length=1, verbose_name='Вік')),
                ('consumer', models.CharField(default='U', choices=[('M', 'Мужчине'), ('W', 'Женщине'), ('U', 'Унисекс')], max_length=1, verbose_name='Пол')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 18, 10, 33, 674495, tzinfo=utc), verbose_name='Дата публікації')),
                ('count', models.SmallIntegerField(default=-1, verbose_name='Кількість')),
                ('visites', models.PositiveIntegerField(default=0, verbose_name='Відвідування')),
                ('buys', models.PositiveIntegerField(default=0, verbose_name='Покупки')),
                ('avatar', models.ImageField(upload_to='goods', verbose_name='Фото')),
                ('base', models.ForeignKey(verbose_name='Основа', to='goods.Bases')),
                ('color', models.ForeignKey(verbose_name='Колір', to='goods.Colors')),
            ],
            options={
                'verbose_name_plural': 'Товари',
                'verbose_name': 'Товар',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('date', models.CharField(max_length=100, help_text='Приклад: c 19 января по 25 марта', verbose_name='Дата проходження')),
            ],
            options={
                'verbose_name_plural': 'Свята',
                'verbose_name': 'Свято',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Матеріали',
                'verbose_name': 'Матеріал',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Styles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Стилі',
                'verbose_name': 'Стиль',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Technics',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Техніки',
                'verbose_name': 'Техніка',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='goods',
            name='holiday',
            field=models.ForeignKey(verbose_name='Свято', to='goods.Holidays'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='material',
            field=models.ManyToManyField(to='goods.Materials', verbose_name='Матеріал'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='style',
            field=models.ForeignKey(verbose_name='Стилі', to='goods.Styles'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='goods',
            name='technic',
            field=models.ForeignKey(verbose_name='Техніка', to='goods.Technics'),
            preserve_default=True,
        ),
    ]
