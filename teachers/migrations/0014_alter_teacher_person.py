# Generated by Django 4.1 on 2022-08-20 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_person_about_me_person_life_credo'),
        ('teachers', '0013_category_mass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='staff.person', verbose_name='Працівник'),
        ),
    ]