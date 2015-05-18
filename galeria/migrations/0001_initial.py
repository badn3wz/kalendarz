# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import audit_log.models.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, editable=False, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='nazwa')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='opis')),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False, related_name='created_galeria_album_set')),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True, editable=False, related_name='modified_galeria_album_set')),
            ],
            options={
                'ordering': ['-pk'],
                'verbose_name_plural': 'albumy',
                'verbose_name': 'album',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('created_with_session_key', audit_log.models.fields.CreatingSessionKeyField(max_length=40, editable=False, null=True)),
                ('modified_with_session_key', audit_log.models.fields.LastSessionKeyField(max_length=40, editable=False, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='nazwa')),
                ('file', sorl.thumbnail.fields.ImageField(upload_to='photos')),
                ('description', models.TextField(blank=True, max_length=5000, verbose_name='opis')),
                ('album', models.ForeignKey(to='galeria.Album')),
                ('created_by', audit_log.models.fields.CreatingUserField(to=settings.AUTH_USER_MODEL, verbose_name='created by', null=True, editable=False, related_name='created_galeria_photo_set')),
                ('modified_by', audit_log.models.fields.LastUserField(to=settings.AUTH_USER_MODEL, verbose_name='modified by', null=True, editable=False, related_name='modified_galeria_photo_set')),
            ],
            options={
                'verbose_name_plural': 'zdjęcia',
                'verbose_name': 'zdjęcie',
            },
            bases=(models.Model,),
        ),
    ]
