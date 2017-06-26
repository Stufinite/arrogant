# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 02:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('infernoWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('raw', models.CharField(max_length=500)),
                ('like', models.PositiveSmallIntegerField(default=0)),
                ('emotion', models.CharField(choices=[('neutral', 'neutral'), ('pos', 'pos'), ('neg', 'neg')], default='neutral', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='', max_length=30)),
                ('banner', models.CharField(default='', max_length=200)),
                ('path', models.CharField(default='', max_length=40)),
                ('area', models.CharField(default='', max_length=10)),
                ('公司規模', models.CharField(default='未公開', max_length=5)),
                ('地址', models.CharField(default='', max_length=40)),
                ('資本額', models.CharField(default='未公開', max_length=10)),
                ('description', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('intern_tf', models.BooleanField(default=False)),
                ('has_salary_info', models.BooleanField(default=False)),
                ('salary', models.CharField(default='未公開', max_length=30)),
                ('path', models.CharField(default='', max_length=40)),
                ('avatar', models.CharField(default='', max_length=200)),
                ('feedback_amount', models.PositiveIntegerField(default=0)),
                ('feedback_freedom', models.FloatField(default=3)),
                ('feedback_FU', models.FloatField(default=3)),
                ('feedback_easy', models.FloatField(default=3)),
                ('feedback_salary', models.FloatField(default=3)),
                ('feedback_knowledgeable', models.FloatField(default=3)),
                ('attendee', models.ManyToManyField(to='infernoWeb.User')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Company')),
            ],
        ),
        migrations.CreateModel(
            name='JobTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('Job', models.ManyToManyField(to='arrogant.Job')),
            ],
        ),
        migrations.CreateModel(
            name='LikesFromUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lfuauthor', to='infernoWeb.User')),
                ('comment', models.ManyToManyField(to='arrogant.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='PageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(default=django.utils.timezone.now)),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ploguser', to='infernoWeb.User')),
            ],
        ),
        migrations.CreateModel(
            name='SkillTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('skill_field', models.CharField(max_length=10)),
                ('Job', models.ManyToManyField(to='arrogant.Job')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together=set([('brand', 'path')]),
        ),
        migrations.AddField(
            model_name='comment',
            name='Job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arrogant.Job'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='cmtauthor', to='infernoWeb.User'),
        ),
    ]
