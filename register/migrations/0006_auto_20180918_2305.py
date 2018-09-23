# Generated by Django 2.1.1 on 2018-09-18 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_competition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='competitor_id',
        ),
        migrations.RemoveField(
            model_name='competition',
            name='regulatory_id',
        ),
        migrations.AddField(
            model_name='competition',
            name='competitor',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='competition',
            name='reg_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='competitor',
            name='username',
            field=models.CharField(blank=True, default='tomakl', max_length=200),
        ),
        migrations.AddField(
            model_name='regulatory',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]