# Generated by Django 2.1.1 on 2018-09-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0026_auto_20180920_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionregister',
            name='start_number',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='Numer startowy'),
        ),
        migrations.AlterField(
            model_name='competitionregister',
            name='time_registered',
            field=models.DateTimeField(verbose_name='Czas rejestracji'),
        ),
    ]
