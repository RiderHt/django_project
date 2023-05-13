# Generated by Django 4.1.7 on 2023-05-06 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_categories_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='users',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.users'),
        ),
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.categories'),
        ),
    ]
