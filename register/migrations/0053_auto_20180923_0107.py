# Generated by Django 2.1.1 on 2018-09-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0052_auto_20180923_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='start_number',
            field=models.IntegerField(verbose_name='Numer startowy'),
        ),
    ]