# Generated by Django 4.1 on 2022-08-20 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageofpage',
            name='data',
            field=models.DateField(auto_now_add=True, verbose_name='Дата завантаження'),
        ),
    ]