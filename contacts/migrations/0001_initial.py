# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Повне Ім’я')),
                ('tel', models.CharField(max_length=20, blank=True, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=75, verbose_name='Email')),
                ('address', models.CharField(max_length=100, help_text='Назва вулиці, номер будинку ', blank=True, verbose_name='Адреса')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Опис')),
                ('avatar', models.ImageField(upload_to='contacts', verbose_name='Фото')),
                ('socialNetwork', models.URLField(help_text='Декілька через /', verbose_name='Cоцмережа')),
                ('isPartner', models.BooleanField(verbose_name='Чи є партнером?')),
            ],
            options={
                'verbose_name_plural': 'Контакти',
                'verbose_name': 'Контакт',
            },
            bases=(models.Model,),
        ),
    ]
