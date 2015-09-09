# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('headline',),
            },
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('expertise', models.CharField(max_length=3, choices=[(b's', b'sport'), (b'p', b'politics'), (b'f', b'finance'), (b's', b'social'), (b'e', b'enviromental'), (b't', b'technology')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='reporter',
            field=models.ForeignKey(related_name='articles', to='articles.Reporter'),
        ),
    ]
