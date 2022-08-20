# Generated by Django 4.1 on 2022-08-20 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0020_person_about_me_person_life_credo'),
        ('teachers', '0011_alter_teacher_lessons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.person', unique=True, verbose_name='Працівник'),
        ),
    ]