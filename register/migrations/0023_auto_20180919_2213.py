# Generated by Django 2.1.1 on 2018-09-19 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0022_auto_20180919_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='comp_allowed',
            field=models.IntegerField(default='0', verbose_name='Limit'),
        ),
        migrations.AddField(
            model_name='competition',
            name='comp_reported',
            field=models.IntegerField(default='0', verbose_name='Zgłoszonych'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='status',
            field=models.SmallIntegerField(choices=[(1, 'Aktywny'), (0, 'Nieaktywny')]),
        ),
    ]