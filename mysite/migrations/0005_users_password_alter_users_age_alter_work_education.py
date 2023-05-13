# Generated by Django 4.1.7 on 2023-04-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_work_alter_addres_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='12345', max_length=70, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(verbose_name='Возраст:'),
        ),
        migrations.AlterField(
            model_name='work',
            name='education',
            field=models.CharField(choices=[('n', ' Среднее профессиональное'), ('a', ' Бакалавриат'), ('t', ' Специалитет, магистратура'), ('e', ' Подготовка кадров высшей квалификации')], max_length=1, verbose_name='Образование:'),
        ),
    ]
