# Generated by Django 2.1.1 on 2018-09-21 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0033_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='competition',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='competitor',
        ),
        migrations.AddField(
            model_name='competitor',
            name='payment',
            field=models.SmallIntegerField(choices=[(0, 'BRAK'), (1, 'OK')], default=0),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
