# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-30 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0006_auto_20170926_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=128)),
                ('customer_phone', models.CharField(blank=True, max_length=128)),
                ('customer_id', models.CharField(blank=True, max_length=128)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
        ),
    ]
