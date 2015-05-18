# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='nazwa')),
                ('importance', models.IntegerField(default=0, verbose_name='waga')),
                ('css_class', models.CharField(blank=True, choices=[('panel-warning', 'warning'), ('panel-info', 'info'), ('panel-success', 'success'), ('panel-danger', 'danger'), ('panel-primary', 'primary'), ('panel-default', 'default')], max_length=50, default='panel-default', verbose_name='klasa css')),
            ],
            options={
                'ordering': ['-importance'],
                'verbose_name_plural': 'stopnie',
                'verbose_name': 'stopień',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('send_mail', models.BooleanField(default=False)),
                ('nick', models.CharField(blank=True, max_length=30, default='', verbose_name='nick profilu')),
                ('player_id', models.CharField(blank=True, max_length=18, validators=[django.core.validators.RegexValidator(regex='^\\d{17}$', code='niepoprawny PID', message='Wpisano niepoprawny numer PID')], verbose_name='player ID', null=True, default='')),
                ('rank', models.ForeignKey(to='playerprofile.Rank', verbose_name='stopień', null=True)),
            ],
            options={
                'verbose_name_plural': 'profile użytkowników',
                'verbose_name': 'profil użytkownika',
            },
            bases=(models.Model,),
        ),
    ]
