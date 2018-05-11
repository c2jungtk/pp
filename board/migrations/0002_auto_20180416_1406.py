# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-16 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(null=True, upload_to='images/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='title',
            field=models.CharField(choices=[('C', '중식'), ('K', '한식'), ('J', '일식'), ('E', '유럽식')], max_length=1, verbose_name='음식'),
        ),
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.Img'),
        ),
    ]