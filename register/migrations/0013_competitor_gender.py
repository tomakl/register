# Generated by Django 2.1.1 on 2018-09-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20180919_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='gender',
            field=models.IntegerField(choices=[('1', 'Mężczyzna'), ('2', 'Kobieta')], default='1', max_length=1, verbose_name='Płeć'),
        ),
    ]
