# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-24 14:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('arrogant', '0001_initial'), ('arrogant', '0002_auto_20170423_2354'), ('arrogant', '0003_job_avatar'), ('arrogant', '0004_auto_20170424_0008'), ('arrogant', '0005_auto_20170424_1605'), ('arrogant', '0006_auto_20170424_1610')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(default=datetime.datetime.now)),
                ('raw', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('職務類別', models.CharField(max_length=20, null=True)),
                ('學歷限制', models.CharField(max_length=20, null=True)),
                ('job', models.CharField(max_length=35)),
                ('聯絡人員', models.CharField(max_length=20, null=True)),
                ('需求人數', models.CharField(max_length=20, null=True)),
                ('工作經驗', models.CharField(max_length=20, null=True)),
                ('到職日期', models.CharField(max_length=20, null=True)),
                ('薪資', models.CharField(max_length=20, null=True)),
                ('地區', models.CharField(max_length=20, null=True)),
                ('科系限制', models.CharField(max_length=20, null=True)),
                ('工作時間', models.CharField(max_length=35, null=True)),
                ('休假制度', models.CharField(max_length=20, null=True)),
                ('工作地點', models.CharField(max_length=20, null=True)),
                ('實習時段', models.CharField(max_length=20, null=True)),
                ('職缺更新', models.CharField(max_length=20, null=True)),
                ('工作性質', models.CharField(max_length=20, null=True)),
                ('url', models.CharField(max_length=100)),
                ('工作說明', models.CharField(max_length=100, null=True)),
                ('身份類別', models.CharField(max_length=20, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Company')),
                ('avatar', models.ImageField(default='politician.png', upload_to='')),
                ('fromWitchWeb', models.CharField(default='1111', max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Job'),
        ),
    ]