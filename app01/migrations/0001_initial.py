# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-06-02 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')], verbose_name='性别')),
                ('info', models.TextField(verbose_name='作者简介')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='书名')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('publish_date', models.DateField(auto_now_add=True, verbose_name='出版日期')),
            ],
        ),
        migrations.CreateModel(
            name='Book2Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=64)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='app01.Book2Author', to='app01.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish', verbose_name='出版社'),
        ),
    ]
