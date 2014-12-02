# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Опис')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2014, 12, 1, 18, 10, 33, 680459, tzinfo=utc), verbose_name='Дата створення')),
                ('avatar', models.ImageField(upload_to='news', verbose_name='Фото')),
                ('workshop', models.ForeignKey(verbose_name='Майстер клас', to='workshops.Workshops')),
            ],
            options={
                'verbose_name_plural': 'Новини',
                'verbose_name': 'Новина',
            },
            bases=(models.Model,),
        ),
    ]
