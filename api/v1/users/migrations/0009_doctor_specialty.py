# Generated by Django 4.0.2 on 2022-04-20 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_patient_dob_remove_patient_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(default='N/A', max_length=255),
            preserve_default=False,
        ),
    ]
