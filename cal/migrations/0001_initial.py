# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('absence', models.BooleanField(verbose_name='nieobecność', default=False)),
            ],
            options={
                'verbose_name': 'zapis',
                'verbose_name_plural': 'zapisy',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='tytuł', max_length=200)),
                ('author', models.CharField(verbose_name='autor', max_length=200)),
                ('datetime', models.DateTimeField(verbose_name='data i czas', default=cal.models.default_start_time)),
                ('url', models.URLField(verbose_name='Link', blank=True)),
                ('is_open', models.BooleanField(verbose_name='otwarte', default=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='stworzone przez', editable=False)),
            ],
            options={
                'verbose_name': 'wydarzenie',
                'ordering': ['datetime'],
                'verbose_name_plural': 'wydarzenia',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='nazwa', max_length=100)),
                ('css_class', models.CharField(verbose_name='klasa css', default='', blank=True, max_length=50, choices=[('list-group-item-warning', 'warning'), ('list-group-item-info', 'info'), ('list-group-item-success', 'success'), ('list-group-item-danger', 'danger'), ('list-group-item-default', 'default')])),
            ],
            options={
                'verbose_name': 'typ wydarzenia',
                'verbose_name_plural': 'Typy wydarzeń',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('group_name', models.CharField(verbose_name='nazwa grupy', blank=True, max_length=50)),
                ('order', models.IntegerField(verbose_name='kolejność', default=0, max_length=20)),
                ('event', models.ForeignKey(verbose_name='wydarzenie', to='cal.Event')),
            ],
            options={
                'verbose_name': 'slot',
                'verbose_name_plural': 'sloty',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SlotType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='nazwa', max_length=100)),
                ('translation', models.CharField(verbose_name='Tłumaczenie', default='', blank=True, max_length=100)),
                ('description', models.TextField(verbose_name='Opis', blank=True, max_length=5000)),
            ],
            options={
                'verbose_name': 'typ slotu',
                'ordering': ['pk'],
                'verbose_name_plural': 'typy slotów',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='nazwa', max_length=50)),
                ('pic', models.ImageField(upload_to='terrains', null=True, blank=True)),
                ('is_active', models.BooleanField(verbose_name='aktywna', default=True)),
            ],
            options={
                'verbose_name': 'mapa',
                'verbose_name_plural': 'mapy',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='slot',
            name='type',
            field=models.ForeignKey(verbose_name='typ', to='cal.SlotType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='terrain',
            field=models.ForeignKey(null=True, blank=True, to='cal.Terrain', verbose_name='Mapa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.ForeignKey(verbose_name='typ', to='cal.EventType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='slot',
            field=models.OneToOneField(to='cal.Slot'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(verbose_name='użytkownik', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
