# Generated by Django 4.0.2 on 2022-04-17 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_patient_height_alter_patient_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='height',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]