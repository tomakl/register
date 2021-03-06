# Generated by Django 2.1.1 on 2018-09-18 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20180918_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='competitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Competitor', verbose_name='Zawodnik'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data rozpoczęcia'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='distance',
            field=models.IntegerField(verbose_name='Dystans'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa zawodów'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='price',
            field=models.IntegerField(verbose_name='Cena'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='reg_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Regulatory', verbose_name='Regulamin'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data urodzenia'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='club',
            field=models.CharField(max_length=200, verbose_name='Klub/Drużyna'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='email',
            field=models.EmailField(blank=True, max_length=70, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='firstname',
            field=models.CharField(max_length=200, verbose_name='Imię'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='lastname',
            field=models.CharField(max_length=200, verbose_name='Nazwisko'),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nazwa użytkownika'),
        ),
        migrations.AlterField(
            model_name='regulatory',
            name='content',
            field=models.TextField(verbose_name='Treść regulaminu'),
        ),
        migrations.AlterField(
            model_name='regulatory',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Utworzono'),
        ),
        migrations.AlterField(
            model_name='regulatory',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Opublikowno'),
        ),
    ]
