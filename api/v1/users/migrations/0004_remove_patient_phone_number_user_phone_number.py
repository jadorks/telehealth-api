# Generated by Django 4.0.2 on 2022-04-10 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_patient_gender_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='0241234567', max_length=20),
            preserve_default=False,
        ),
    ]
