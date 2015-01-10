# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('youtube_url', models.URLField()),
                ('year', models.IntegerField(default=2000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(related_name='genre', to='songs.Genre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
