# Generated by Django 2.1.1 on 2018-09-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_competition_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='image',
            field=models.ImageField(blank='True', upload_to='register/media/events'),
        ),
    ]