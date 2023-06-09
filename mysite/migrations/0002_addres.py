# Generated by Django 4.1.7 on 2023-04-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=30, verbose_name='Регион')),
                ('town', models.CharField(max_length=15, verbose_name='Город')),
                ('street', models.CharField(max_length=10, verbose_name='Улица')),
                ('house', models.ImageField(max_length=10, upload_to='', verbose_name='Номер дома')),
            ],
        ),
    ]
