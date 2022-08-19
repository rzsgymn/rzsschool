# Generated by Django 4.1 on 2022-08-19 08:39

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='json',
            field=models.JSONField(default=core.models.jsonfield_default_value, help_text='Для зручної роботи з JSON використовуйте JSONReader https://jsonformatter.org/'),
        ),
    ]